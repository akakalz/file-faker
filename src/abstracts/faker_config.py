from dataclasses import dataclass
from typing import Any, List


@dataclass(frozen=True)
class FileFakerConfig:
    file_name: str
    fields: List[Any]
    has_header: bool
    row_count: int
    delimiter: str = ""
    fixed_width: int = 0
    output_path: str = None
    eol: str = "\n"
