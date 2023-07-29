from pathlib import Path

import yaml

from autoclonegit.exceptions import YamlFileNotExistsException


class YamlParser:
    def __init__(self, file_path: str) -> None:
        file = Path(file_path)

        if not file.exists():
            raise YamlFileNotExistsException(f"File {file_path} not found!")

        self.yaml_file = file

    def get_content_dict(self) -> dict:
        with self.yaml_file.open("r") as file:
            content_dict = yaml.safe_load(file)

        return content_dict
