from pathlib import Path
from typing import Optional

import typer

import autogit


app = typer.Typer()


def print_bye_message() -> None:
    typer.echo("")
    typer.echo("┌──────────────────────────────┐")
    typer.echo("│ Thanks for use AutoGit. Bye! │")
    typer.echo("└──────────────────────────────┘")


def run_process(file: str, dest_folder: str, action: str) -> None:
    try:
        autogit_ = autogit.AutoGit(file=file, dest_folder=dest_folder)

    except autogit.FileDoesNotExists as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(1)

    except autogit.DestFolderException as e:
        typer.secho(str(e), fg=typer.colors.RED)
        raise typer.Exit(1)

    getattr(autogit_, action)()

    print_bye_message()

    raise typer.Exit()


@app.command(help="Clone git repositories.")
def clone(
    file: str = typer.Argument(
        default=None,
        help="Yaml file with the Git repositories to clone.",
    ),
    dest_folder: str = typer.Option(
        str(Path.home()),
        "--dest-folder",
        "-d",
        help="Folder used to clone the Git repositories.",
    ),
) -> None:

    run_process(file, dest_folder, "clone")


@app.command(help="Pull git repositories.")
def pull(
    file: str = typer.Argument(
        default=None,
        help="Yaml file with the Git repositories to pull.",
    ),
    dest_folder: str = typer.Option(
        str(Path.home()),
        "--dest-folder",
        "-d",
        help="Folder used to pull the Git repositories.",
    ),
) -> None:

    run_process(file, dest_folder, "pull")


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{autogit.__app_name__} version {autogit.__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:

    return
