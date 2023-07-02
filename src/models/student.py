"""
Contains a student's class describing the application's data model

version: 1.0.0

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
from models.currency import Currency
from models.student_state import StudentState


class Student:
    _NAME: str = None
    _HOUR_COST: float = 0
    _CURRENCY: Currency = None  # unchanged attribute
    _STATE: str = None
    _TABLE: str = None  # unchanged attribute

    def __init__(self, name, hour_cost, currency, state, table):
        # set changed attributes
        self.set_name(name)
        self.set_hour_cost(hour_cost)
        self.set_currency(currency)

        # set unchanged attributes
        assert StudentState.is_student_state(state), \
            f"Student state is invalid. Find {state} need one of {StudentState.all()}"
        self._STATE = StudentState.get_student_state(state)

        assert table is not None, "Student table name is None"
        assert isinstance(table, str), f"Student table name is {type(name)}, not str"
        assert len(table) > 0, 'Student table name is empty'
        self._TABLE = str(name)

    def name(self) -> str:
        return self._NAME

    def set_name(self, name):
        assert name is not None, "Student name is None"
        assert isinstance(name, str), f"Student name is {type(name)}, not str"
        assert len(name) > 0, 'Student name is empty'
        self._NAME = str(name)

    def hour_cost(self) -> float:
        return self._HOUR_COST

    def set_hour_cost(self, hour_cost):
        assert isinstance(hour_cost, (int, float,)), \
            f"Student {self._NAME} hour cost is {type(hour_cost)} not float or int"
        assert hour_cost >= 0, f"Student {self._NAME} hour cost is low than zero"

        self._HOUR_COST = float(hour_cost)

    def currency(self) -> Currency:
        return self._CURRENCY

    def set_currency(self, currency):
        assert Currency.is_currency(currency), \
            f"Student currency is invalid. Find {currency} need one of {Currency.all()}"
        self._CURRENCY = Currency.get_currency(currency)

    def state(self) -> StudentState:
        return self._STATE

    def table(self) -> str:
        return self._TABLE

    @staticmethod
    def create_new_student(name, hour_cost, currency, state):
        return Student(name, hour_cost, currency, state, f'table_{name}_{str(currency.value).lower()}')
