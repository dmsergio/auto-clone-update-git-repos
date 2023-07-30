from pathlib import Path

import typer
import yaml

from autogit.exceptions import DestFolderException
from autogit.exceptions import FileDoesNotExists


class AutoGit:
    def __init__(self, file: str, dest_folder: str) -> None:
        self.file = file
        self.dest_folder = dest_folder

    @property
    def error(self) -> int:
        return self.__error

    @property
    def file(self) -> Path:
        return self._file

    @file.setter
    def file(self, value: str) -> None:
        file = Path(value)

        if not file.exists():
            raise FileDoesNotExists(f"File '{file}' not found!")

        self._file = file

    @property
    def dest_folder(self) -> Path:
        return self._dest_folder

    @dest_folder.setter
    def dest_folder(self, value: str) -> None:
        folder = Path(value)

        try:
            folder.mkdir(exist_ok=True)

        except OSError:
            raise DestFolderException(f"Folder '{value}' not found!")

        self._dest_folder = folder

    def __get_file_content(self) -> dict:
        with self._file.open("r") as content:
            content_dict = yaml.safe_load(content)

        print(content_dict)
        return content_dict

    def clone(self) -> None:
        content_dict = self.__get_file_content()
        total_repos = len(content_dict)

        typer.secho(
            f"{total_repos} repos to clone in '{self.dest_folder}'",
            fg=typer.colors.BRIGHT_BLUE,
        )

        for i, (repo, (origin, branch, depth)) in enumerate(content_dict.items(), 1):
            header = f"Repository {repo} ({i} / {total_repos})"
            typer.secho("\n" + header, fg=typer.colors.BRIGHT_BLUE)
            typer.secho("=" * len(header), fg=typer.colors.BRIGHT_BLUE)

            repo_folder = self.dest_folder / repo

            if self.__exists_repo_folder(repo_folder):
                typer.secho(
                    f"'{repo}' repository skip, already exists.",
                    fg=typer.colors.BRIGHT_YELLOW,
                )

            origin_ = content_dict[repo][origin]
            branch_ = content_dict[repo][branch]
            depth_ = content_dict[repo][depth]

            command = f"git clone --depth {depth_} --branch {branch_} {origin_} {repo_folder}"
            typer.secho(command, fg=typer.colors.RESET)

    def __exists_repo_folder(self, repo_folder: str) -> bool:
        return repo_folder.exists()

    def pull(self) -> None:
        ...
