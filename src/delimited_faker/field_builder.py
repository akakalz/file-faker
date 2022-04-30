from typing import Callable
from faker import Faker


class FieldBuilder:
    __slots__ = [
        "format_func",
        "faker_method",
    ]

    def __init__(self, faker: Faker, faker_method: str, format_func: Callable = lambda x: str(x)) -> None:
        self.format_func = format_func
        self.faker_method = getattr(faker, faker_method)

    def __repr__(self) -> str:
        return self.format_func(self.faker_method())

    def __str__(self) -> str:
        return self.format_func(self.faker_method())
