"""
Contains a student's class describing the application's data model

version: 1.1.1

versions-list:  1.0.0 - start valid version(can initialize Student class and create new Student objects)
                1.0.1 - add some magic methods(__eq__, __ne__, __str__, __repr__, __hash__)
                1.1.1 - on line 34 from self._TABLE = str(name) to self._TABLE = str(table)

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
from models.currency import Currency


class Student:
    _NAME: str = None
    _HOUR_COST: float = 0
    _CURRENCY: Currency = None  # unchanged attribute
    _TABLE: str = None  # unchanged attribute

    def __init__(self, name, hour_cost, currency, table):
        # set changed attributes
        self.set_name(name)
        self.set_hour_cost(hour_cost)

        # set unchanged attributes
        assert Currency.is_currency(currency), \
            f"Student currency is invalid. Find {currency} need one of {Currency.all()}"
        self._CURRENCY = Currency.get_currency(currency)

        assert table is not None, "Student table name is None"
        assert isinstance(table, str), f"Student table name is {type(name)}, not str"
        assert len(table) > 0, 'Student table name is empty'
        self._TABLE = str(table)

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
        assert hour_cost > 0, f"Student {self._NAME} hour cost must be more than zero"

        self._HOUR_COST = float(hour_cost)

    def currency(self) -> Currency:
        return self._CURRENCY

    def table(self) -> str:
        return self._TABLE

    def __eq__(self, o: object) -> bool:
        if o is None:
            return False

        if o is self:
            return True

        if not isinstance(o, self.__class__):
            return False

        # if db tables for students visits is eq or student's names is eq than students eq
        return self.table() == o.table() or self.name() == o.name()

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __str__(self) -> str:
        return f'Student<name={self.name()} hour-cost={self.hour_cost()} currency={self.currency()}>'

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        _hash = hash(self.__class__.__name__)
        _hash = 31 * _hash + hash(self.name())
        _hash = 31 * _hash + hash(self.currency())
        _hash = 31 * _hash + hash(self.table())
        return _hash

    @staticmethod
    def create_new_student(name, hour_cost, currency):
        return Student(name, hour_cost, currency, f'table_{name}_{str(currency).lower()}')
