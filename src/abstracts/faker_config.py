from dataclasses import dataclass
from typing import List, Union
from abstracts.field import FixedWidthField, DelimitedField


@dataclass(frozen=True)
class FileFakerConfig:
    file_name: str
    fields: List[Union[FixedWidthField, DelimitedField]]
    has_header: bool
    row_count: int
    delimiter: str = ""
    fixed_width: int = 0
    output_path: str = None
    eol: str = "\n"
