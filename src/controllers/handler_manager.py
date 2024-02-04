"""
Contains the main control functions for working with the database and models:
a set of students and a list of visits by students

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import typing

from settings import RuntimeSettings
from controllers.database import DataBase, Student, Visit


class HandlerManager:

    def __init__(self, settings: RuntimeSettings, database: DataBase):
        self._settings = settings
        self._db = database
        self._current_student_index = 0
        self._archive_mode = False

    @property
    def archive_mode(self) -> bool:
        return self._archive_mode

    @archive_mode.setter
    def archive_mode(self, value: bool) -> None:
        self._archive_mode = bool(value)

    def get_current_student(self) -> typing.Optional[Student]:
        if self._is_valid_index():
            return self._db.students[self._current_student_index]

        return None

    def _is_valid_index(self) -> bool:
        return 0 <= self._current_student_index < len(self._db.students)

    def get_current_student_visits(self) -> list[Visit]:
        student: Student = self.get_current_student()
        if student is None:
            return []

        return self._db.get_student_visits(student)

    def delete_current_student(self):
        student = self.get_current_student()
        if student is not None:
            self._db.remove_student(student, is_archive_mode=self.archive_mode)

        # normalised current student index
        if len(self._db.students) == 0:
            self._current_student_index = 0
            return

        while self._current_student_index >= len(self._db.students):
            self.prev_student()

    def next_student(self):
        if len(self._db.students) == 0:
            return

        self._current_student_index = (self._current_student_index + 1) % len(self._db.students)

    def prev_student(self):
        if len(self._db.students) == 0:
            return

        self._current_student_index = (self._current_student_index - 1) % len(self._db.students)

    def set_current_index(self, index):
        if not (0 <= index < len(self._db.students)):
            return
        print(index)
        self._current_student_index = index

    def delete_student_visit(self, visit: Visit):
        student = self.get_current_student()
        if student is None:
            return

        self._db.remove_student_visit(student, visit)

    def get_students(self) -> tuple[Student]:
        return tuple(self._db.get_students(is_archive_mode=self.archive_mode))

    def get_student_visits(self, student: Student) -> list[Visit]:
        if student is None or not isinstance(student, Student):
            return []

        return self._db.get_student_visits(student)

    def archivate_student(self, student: Student):
        self._db.archive_student(student, is_archive_mode=self.archive_mode)

    def get_current_index(self):
        return self._current_student_index
