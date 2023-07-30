from pathlib import Path

import yaml

from autogit.exceptions import YamlFileDoesNotExists


class YamlParser:
    def __init__(self, file_path: str) -> None:
        file = Path(file_path)

        if not file.exists():
            raise YamlFileDoesNotExists(f"File {file_path} not found!")

        self.yaml_file = file

    def get_content_dict(self) -> dict:
        with self.yaml_file.open("r") as file:
            content_dict = yaml.safe_load(file)

        return content_dict
