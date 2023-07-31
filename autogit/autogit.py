import subprocess
from pathlib import Path

import typer
import yaml

from autogit.exceptions import DestFolderException
from autogit.exceptions import FileDoesNotExists


class AutoGit:
    def __init__(self, file: str, dest_folder: str) -> None:
        self.file = file
        self.dest_folder = dest_folder
        self.success_total = 0
        self.skipped_total = 0
        self.error_total = 0
        self.__command = None

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
                    f"'{repo}' repository skipped, already exists.",
                    fg=typer.colors.BRIGHT_YELLOW,
                )
                self.skipped_total += 1
                continue

            origin_ = content_dict[repo][origin]
            branch_ = content_dict[repo][branch]
            depth_ = content_dict[repo][depth]

            self.__command = (
                f"git clone --depth {depth_} --branch {branch_} {origin_} {repo_folder}"
            )
            try:
                self.__exec_command(action="Clonning")

            except Exception as e:
                typer.secho(f"Error {e}", fg=typer.colors.BRIGHT_RED)
                self.error_total += 1
                continue

            self.success_total += 1

        self.__print_resume()
        self.__reset_total_values()
        self.__print_bye_message("Clone")

    def __exists_repo_folder(self, repo_folder: str) -> bool:
        return repo_folder.exists()

    def __exec_command(self, action: str) -> None:
        if self.__command is not None:
            typer.secho(f"{action} in '{self.dest_folder}' ...")

            with subprocess.Popen(
                self.__command.split(),
                cwd=self.dest_folder,
                stdout=subprocess.PIPE,
            ) as process:

                while process.poll() is None:
                    typer.secho(process.stdout.read1().decode("utf-8"))

            self.__command = None

    def __print_bye_message(self, action: str) -> None:
        typer.secho(f"\n{action} command finished!")

    def __print_resume(self) -> None:
        if self.success_total:
            literal = "repository" if self.success_total == 1 else "repositories"
            typer.secho(
                f"\n{self.success_total} {literal} cloned successfully.",
                fg=typer.colors.BRIGHT_GREEN,
            )

        if self.skipped_total:
            literal = "repository" if self.skipped_total == 1 else "repositories"
            typer.secho(
                f"\n{self.skipped_total} {literal} skipped.",
                fg=typer.colors.BRIGHT_YELLOW,
            )

        if self.error_total:
            literal = "repository" if self.error_total == 1 else "repositories"
            typer.secho(
                f"\n{self.error_total} {literal} don't cloned by some error.",
                fg=typer.colors.BRIGHT_RED,
            )

    def __reset_total_values(self):
        self.success_total, self.skipped_total, self.error_total = 0, 0, 0

    def pull(self) -> None:
        ...
