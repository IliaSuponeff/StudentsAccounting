"""
Contains class implementing a sqlite-database connection

version: 0.0.3

versions-list:  0.0.1 - setup standard db functions(execution sql scripts and get their results)
                0.0.2 - adding external control functions
                0.0.3 - adding functions to add/remove students to/from db

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import sqlite3
import sys

from settings import RuntimeSettings
from jinja2 import Template
from models.student import Student
from models.student_visit import Visit


class DataBase:
    NONE_RESULT = 0
    ONE_RESULT = 1
    ALL_RESULTS = -1

    def __init__(self, settings: RuntimeSettings):
        self.settings = settings

        # build connection to db
        self._connection = sqlite3.connect(self.settings.get_resource_filepath('db.sqlite'))
        self._cursor = self._connection.cursor()

        # try to initialize db
        self._execute_script('.init_db')
        self.students = self.get_students()

        if self.settings.debug():
            print(f"Students: {self.students}", file=sys.stderr)

    def close(self):
        self.save()
        self._cursor.close()
        self._connection.close()

    def add_student(self, student: Student):
        if student in self.students:
            raise AssertionError(f"Student {student.name()} is exists now")
        else:
            self.students.append(student)

        self._execute_script(
            'add_student',
            name=student.name(),
            hour_cost=student.hour_cost(),
            currency=student.currency().value,
            table=student.table()
        )
        self._execute_script(
            'add_student_table',
            table=student.table()
        )
        self.save()

    def edit_student(self, old_student: Student, new_student: Student):
        # change students list
        index = self.students.index(old_student)
        self.students[index] = new_student

        # reload students DB table
        self._execute_script(
            'edit_student',
            name=new_student.name(),
            hour_cost=new_student.hour_cost(),
            currency=new_student.currency().value,
            table=new_student.table(),
            rowid=index + 1
        )
        visits = self.get_student_visits(old_student)
        self._execute_script('remove_student_table', table=old_student.table())
        self._execute_script('add_student_table', table=new_student.table())

        for visit in visits:
            self.add_student_visit(new_student, visit)

    def remove_student(self, student: Student):
        if not (student in self.students):
            # nothing to do
            return

        self.students.remove(student)
        self._execute_script('remove_student', table=student.table())
        self._execute_script('remove_student_table', table=student.table())

    def add_student_visit(self, student: Student, visit: Visit):
        if visit in self.get_student_visits(student):
            raise AssertionError(
                f"Visit {visit.date().strftime('%d.%m.%Y')} with timespan {visit.timespan()}"
                f"{f' and sum={visit.special_sum()}' if visit.is_special() else ''} is exists now."
            )

        self._execute_script(
            'add_student_visit',
            table=student.table(),
            date=visit.date().strftime('%d.%m.%Y'),
            timespan=visit.timespan(),
            is_special=visit.is_special(),
            special_sum=visit.special_sum()
        )
        self._sort_student_visits(student)

    def edit_student_visit(self, student: Student, old_visit, new_visit: Visit):
        visits = self.get_student_visits(student)
        index = visits.index(old_visit)
        visits[index] = new_visit
        self._execute_script(
            'edit_student_visit',
            table=student.table(),
            date=new_visit.date().strftime('%d.%m.%Y'),
            timespan=new_visit.timespan(),
            is_special=new_visit.is_special(),
            special_sum=new_visit.special_sum(),
            rowid=index + 1
        )
        self._sort_student_visits(student)

    def remove_student_visit(self, student: Student, visit: Visit):
        self._execute_script(
            'remove_student_visit',
            table=student.table(),
            date=visit.date().strftime('%d.%m.%Y'),
            timespan=visit.timespan(),
            is_special=visit.is_special(),
            special_sum=visit.special_sum()
        )

    def remove_student_visit_by_rowid(self, student: Student, rowid: int):
        self._execute_script(
            'remove_student_visit_by_rowid',
            table=student.table(),
            rowid=int(rowid)
        )

    def _sort_student_visits(self, student: Student):
        visits = self.get_student_visits(student)
        visits.sort()
        self._execute_script('remove_student_table', table=student.table())
        self._execute_script('add_student_table', table=student.table())

        for visit in visits:
            self._execute_script(
                'add_student_visit',
                table=student.table(),
                date=visit.date().strftime('%d.%m.%Y'),
                timespan=visit.timespan(),
                is_special=visit.is_special(),
                special_sum=visit.special_sum()
            )

    def get_students(self) -> list[Student]:
        self._execute_script('get_students')
        return [Student(*row) for row in self._get_results(self.ALL_RESULTS)]

    def get_student_visits(self, student: Student) -> list[Visit]:
        self._execute_script(
            'get_student_visits',
            table=student.table()
        )
        return [Visit(*row) for row in self._get_results(self.ALL_RESULTS)]

    def _execute_script(self, script_name: str, **kwargs):
        script_data = self.settings.get_sql_script_filedata(f'{script_name}.sql')
        script_template = Template(script_data)
        script = script_template.render(kwargs)

        if self.settings.debug():
            print(script, file=sys.stderr)

        self._cursor.execute(script)

    def _get_results(self, count: int = 0):
        if count == self.NONE_RESULT:
            return ()

        if count == self.ONE_RESULT:
            return self._cursor.fetchone()

        if count <= self.ALL_RESULTS:
            return self._cursor.fetchall()

        return self._cursor.fetchmany(count)

    def save(self):
        self._connection.commit()
