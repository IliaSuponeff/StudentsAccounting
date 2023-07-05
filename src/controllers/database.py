"""
Contains class implementing a sqlite-database connection

version: 0.0.3

versions-list:  0.0.1 - setup standard db functions(execution sql scripts and get their results)
                0.0.2 - adding external control functions
                0.0.3 - adding functions to add/remove students to/from db

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import pprint
import sqlite3
import sys

from settings import RuntimeSettings
from jinja2 import Template
from models.student import Student, Currency
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

    def remove_student(self, student: Student):
        if not (student in self.students):
            # nothing to do
            return

        self.students.remove(student)
        self._execute_script('remove_student', table=student.table())
        self._execute_script('remove_student_table', table=student.table())

    def add_student_visit(self, student: Student, visit: Visit):
        self._execute_script(
            'add_student_visit',
            table=student.table(),
            date=visit.date(),
            timespan=visit.timespan(),
            is_special=visit.is_special(),
            special_sum=visit.special_sum()
        )

    def remove_student_visit(self, student: Student, visit: Visit):
        self._execute_script(
            'remove_student_visit',
            table=student.table(),
            date=visit.date(),
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
