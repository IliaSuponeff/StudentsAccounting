"""
Contains all currencies supported by the application as an enumeration class

version: 1.0.0

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import enum


class Currency(enum.Enum):
    BYN = 'BYN'
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'

    @staticmethod
    def is_currency(value: str):
        if value is None:
            return False

        if isinstance(value, Currency):
            return True

        value = str(value).lower()
        for item in Currency:
            if item.value.lower() == value:
                return True

        return False

    @staticmethod
    def get_currency(value: str):
        if value is None:
            return None

        if isinstance(value, Currency):
            return value

        value = str(value).lower()
        for item in Currency:
            if item.value.lower() == value:
                return item

        return None

    @staticmethod
    def currency(value: str):
        if value is None:
            return False, None

        if isinstance(value, Currency):
            return True, value

        value = str(value).lower()
        for item in Currency:
            if item.value.lower() == value:
                return True, item

        return False, None

    @staticmethod
    def all():
        return [item.value for item in Currency]

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)
