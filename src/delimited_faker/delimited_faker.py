from typing import List
import csv

from abstracts.faker_config import FileFakerConfig
from abstracts.field import FieldType
from abstracts.file_faker import FileFaker
from .field_builder import FieldBuilder


class DelimitedFaker(FileFaker):
    def __init__(self, config: FileFakerConfig, seeds: List[str] = None) -> None:
        super().__init__(config, seeds)
        self._create_field_builers()

    def _create_field_builers(self) -> None:
        self._func_map = {
            FieldType.address_line_1: FieldBuilder(self._faker, "street_address"),
            FieldType.address_line_2: "",
            FieldType.address_city: FieldBuilder(self._faker, "city"),
            FieldType.address_state: FieldBuilder(self._faker, "country_code"),
            FieldType.address_zip: FieldBuilder(self._faker, "postcode"),
            FieldType.address_zip_ext: "",
            FieldType.currency: FieldBuilder(self._faker, "pricetag", lambda x: x.replace("$", "").replace(",", "")),
            FieldType.date: FieldBuilder(self._faker, "date"),
            FieldType.datetime: FieldBuilder(self._faker, "date_time"),
            FieldType.email: FieldBuilder(self._faker, "email"),
            FieldType.integer: FieldBuilder(self._faker, "random_digit"),
            FieldType.string: FieldBuilder(self._faker, "text", lambda x: x.replace("\n", " ")),
            FieldType.uuid: FieldBuilder(self._faker, "uuid4"),
            FieldType.name: FieldBuilder(self._faker, "name"),
            FieldType.dob: FieldBuilder(self._faker, "date_of_birth"),
        }

    def _fake_without_seed_list(self) -> None:
        with open(self._out_file, "w") as out_file:
            csv_writer = csv.writer(out_file, delimiter=self.config.delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if self.config.has_header:
                csv_writer.writerow([x.name for x in self.config.fields])
            csv_writer.writerows([
                [self._func_map[field.type] for field in self.config.fields]
                for _ in range(self.config.row_count)
            ])

    def _fake_with_seed_list(self) -> None:
        with open(self._out_file, "w") as out_file:
            if self.config.has_header:
                out_file.write(self._build_header())
            for i in range(self.config.row_count):
                self._faker.seed_instance(self._seeds[i])
                out_file.writerow(self._build_line())
