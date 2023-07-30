import pytest
from typer.testing import CliRunner

from autogit import __app_name__
from autogit import __version__
from autogit import cli


runner = CliRunner()

@pytest.mark.parametrize("command", ["--version", "-v"])
def test_version(command):
    result = runner.invoke(cli.app, [command])

    assert result.exit_code is 0
    assert result.stdout == f"{__app_name__} v{__version__}\n"
