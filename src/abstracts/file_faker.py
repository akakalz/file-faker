from abc import ABC, abstractmethod
from faker import Faker
from typing import List
from os import path
from abstracts.faker_config import FileFakerConfig


class FileFaker(ABC):
    __slots__ = [
        "config",
        "_faker",
        "_out_file",
        "_seeds",
    ]

    def __init__(self, config: FileFakerConfig, seeds: List[str] = None) -> None:
        self.config = config

        if self.config.output_path:
            self._out_file = path.join(self.config.output_path, self.config.file_name)
        else:
            self._out_file = self.config.file_name

        self._faker = Faker("en_US")
        self._seeds = seeds

    def fake(self) -> str:
        """
        outputs the path to the file
        """
        if self._seeds:
            self._fake_with_seed_list()
        else:
            self._fake_without_seed_list()
        return self._out_file

    @abstractmethod
    def _fake_with_seed_list(self) -> None:
        ...

    @abstractmethod
    def _fake_without_seed_list(self) -> None:
        ...
