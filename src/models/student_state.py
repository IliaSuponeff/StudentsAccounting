"""
Contains all the student states in the application system in the form of an enumeration class

version: 1.0.0

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import enum


class StudentState(enum.Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

    @staticmethod
    def is_student_state(value: str):
        if value is None:
            return False

        if isinstance(value, StudentState):
            return True

        value = str(value).lower()
        for item in StudentState:
            if item.value.lower() == value:
                return True

        return False

    @staticmethod
    def get_student_state(value: str):
        if value is None:
            return None

        if isinstance(value, StudentState):
            return value

        value = str(value).lower()
        for item in StudentState:
            if item.value.lower() == value:
                return item

        return None

    @staticmethod
    def student_state(value: str):
        if value is None:
            return False, None

        if isinstance(value, StudentState):
            return True, value

        value = str(value).lower()
        for item in StudentState:
            if item.value.lower() == value:
                return True, item

        return False, None

    @staticmethod
    def all():
        return [item.value for item in StudentState]

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)
