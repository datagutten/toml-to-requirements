from __future__ import annotations
import pytest
from toml_to_requirements.main import main
from toml_to_requirements.cli import CLIArguments
from pathlib import Path

EXAMPLE_TOML_PATH = Path("tests/example_toml.toml")
EXAMPLE_REQUIREMENTS_PATH = Path("tests/example_requirements.txt")


@pytest.fixture()
def arguments() -> CLIArguments:
    return CLIArguments(
        toml_file_path=EXAMPLE_TOML_PATH,
        requirements_file_path=EXAMPLE_REQUIREMENTS_PATH,
        optional_lists=["dev"],
        poetry=False,
    )


def test_main(arguments: CLIArguments) -> None:
    try:
        main(arguments)

        assert EXAMPLE_REQUIREMENTS_PATH.is_file()

        with EXAMPLE_REQUIREMENTS_PATH.open("r") as f:
            requirements_content: str = f.read()

        packages_in_requirements = set(requirements_content.split("\n"))

        assert "black" in packages_in_requirements
        assert "toml" in packages_in_requirements
        assert len(packages_in_requirements) == 2
    finally:
        EXAMPLE_REQUIREMENTS_PATH.unlink(missing_ok=True)
