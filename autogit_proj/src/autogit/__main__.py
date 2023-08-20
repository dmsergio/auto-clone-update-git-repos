"""Auto Git fetch entry point script."""

import autogit


def main() -> None:
    autogit.app(prog_name=autogit.__app_name__)


if __name__ == "__main__":
    main()
