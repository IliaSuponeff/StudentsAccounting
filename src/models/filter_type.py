"""
Contains all supported filter types by application as an enumeration class

version: 0.0.1

author: Ilia Suponev GitHub: https://github.com/ProgKalm
"""
import enum


class FilterType(enum.Enum):
    ALL_DAYS = "ALL_DAYS"
    THIS_MONTH = "THIS_MONTH"
    THIS_YEAR = "THIS_YEAR"
    CUSTOM_PERIOD = "CUSTOM_PERIOD"

    @staticmethod
    def is_fiter_type(value: str):
        if value is None:
            return False

        if isinstance(value, FilterType):
            return True

        value = str(value).lower()
        for item in FilterType:
            if item.value.lower() == value:
                return True

        return False

    @staticmethod
    def get_fiter_type(value: str):
        if value is None:
            return None

        if isinstance(value, FilterType):
            return value

        value = str(value).lower()
        for item in FilterType:
            if item.value.lower() == value:
                return item

        return None

    @staticmethod
    def filter_type(value: str):
        if value is None:
            return False, None

        if isinstance(value, FilterType):
            return True, value

        value = str(value).lower()
        for item in FilterType:
            if item.value.lower() == value:
                return True, item

        return False, None

    @staticmethod
    def all() -> list[str]:
        return [item.value for item in FilterType]

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)
