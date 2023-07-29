import pytest
from typer.testing import CliRunner

from autoclonegit import __app_name__
from autoclonegit import __version__
from autoclonegit import cli


runner = CliRunner()

@pytest.mark.parametrize("command", ["--version", "-v"])
def test_version(command):
    result = runner.invoke(cli.app, [command])

    assert result.exit_code is 0
    assert result.stdout == f"{__app_name__} v{__version__}\n"
