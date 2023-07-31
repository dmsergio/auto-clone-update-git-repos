"""Auto Git fetch entry point script."""

from autogit import __app_name__
from autogit import cli


def main() -> None:
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()