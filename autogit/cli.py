from typing import Optional

import typer

from autogit import __app_name__
from autogit import __version__


app = typer.Typer()

@app.command()
def clone(
    file: str = typer.Argument(
        default=None,
        help="Yaml file with the Git repositories to clone.",
    ),
    dest_folder: str = typer.Option(
        ".",
        "--dest-folder",
        "-d",
        help="Folder used to clone the Git repositories."
    ),
) -> None:

    typer.echo(file)
    raise typer.Exit()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
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
