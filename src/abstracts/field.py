from dataclasses import dataclass
from typing import Union


class FieldType:
    string: str = "string"
    integer: str = "integer"
    currency: str = "currency"
    date: str = "date"
    dob: str = "dob"
    datetime: str = "datetime"
    uuid: str = "uuid"
    name: str = "name"
    address_line_1: str = "address_line_1"
    address_line_2: str = "address_line_2"
    address_city: str = "address_city"
    address_state: str = "address_state"
    address_zip: str = "address_zip"
    address_zip_ext: str = "address_zip_ext"
    email: str = "email"


@dataclass
class FixedWidthField:
    name: str
    type: Union[FieldType, str]
    length: int
    format: str = None


@dataclass
class DelimitedField:
    name: str
    type: Union[FieldType, str]
    format: str = None
    length: int = 0
