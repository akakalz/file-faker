from dataclasses import dataclass
from faker import Faker
from typing import List, Union, Optional
from os import path
import csv


class FileType:
    delimited: str = "delimited"
    fixed_width: str = "fixed_width"


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


@dataclass
class FileFakerConfig:
    file_name: str
    file_type: FileType
    fields: Union[List[DelimitedField], List[FixedWidthField]]
    has_header: bool
    row_count: int
    delimiter: str = ""
    fixed_width: int = 0
    output_path: str = None
    seed_list: Optional[List[str]] = None
    eol: str = "\n"


class FileFaker:
    def __init__(self, config: FileFakerConfig, seed: str = None) -> None:
        self.config = config

        if self.config.output_path:
            self._out_file = path.join(self.config.output_path, self.config.file_name)
        else:
            self._out_file = self.config.file_name

        self._joiner = self.config.delimiter if self.config.file_type == FileType.delimited else ""
        self._faker = Faker("en_US")
        # Faker(seed)

    def fake(self) -> str:
        """
        outputs the path to the file
        """
        if self.config.seed_list:
            self._fake_with_seed_list()
        else:
            self._fake_without_seed_list()
        return self._out_file

    def _fake_with_seed_list(self) -> None:
        with open(self._out_file, "w") as out_file:
            if self.config.has_header:
                out_file.write(self._build_header())
            for i in range(self.config.row_count):
                out_file.write(self._build_line(self.config.seed_list[i]))
                out_file.write(self.config.eol)

    def _fake_without_seed_list(self) -> None:
        with open(self._out_file, "w") as out_file:
            csv_writer = csv.writer(out_file, delimiter=self.config.delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if self.config.has_header:
                csv_writer.writerow(self._build_header())
            for _ in range(self.config.row_count):
                csv_writer.writerow(self._build_line())

    def _build_field(self, field_config: Union[DelimitedField, FixedWidthField]) -> str:
        """
        outputs a specific field for a line
        """
        if self._joiner:
            if field_config.type == FieldType.address_line_1:
                return self._faker.street_address()
            elif field_config.type == FieldType.address_line_2:
                return ""
            elif field_config.type == FieldType.address_city:
                return self._faker.city()
            elif field_config.type == FieldType.address_state:
                return self._faker.country_code()
            elif field_config.type == FieldType.address_zip:
                return self._faker.postcode()
            elif field_config.type == FieldType.address_zip_ext:
                return ""
            elif field_config.type == FieldType.currency:
                return self._faker.pricetag().replace("$", "").replace(",", "")
            elif field_config.type == FieldType.date:
                return self._faker.date()
            elif field_config.type == FieldType.datetime:
                return str(self._faker.date_time())
            elif field_config.type == FieldType.email:
                return self._faker.email()
            elif field_config.type == FieldType.integer:
                return self._faker.random_digit()
            elif field_config.type == FieldType.string:
                return self._faker.text().replace("\n", " ")
            elif field_config.type == FieldType.uuid:
                return self._faker.uuid4()
            elif field_config.type == FieldType.name:
                return self._faker.name()
            elif field_config.type == FieldType.dob:
                return self._faker.date_of_birth()
        else:
            raise NotImplementedError("build field is not yet implemented for fixed width files")

    def _build_line(self, line_seed: str = None) -> list:
        """
        outputs a specific line
        """
        fields = []
        if line_seed:
            Faker.seed(line_seed)
        for field in self.config.fields:
            fields.append(self._build_field(field))
        return fields

    def _build_header(self) -> list:
        if self._joiner:
            return [
                x.name
                for x in self.config.fields
            ]
        else:
            raise NotImplementedError("build header is not yet implemented for fixed width files")
