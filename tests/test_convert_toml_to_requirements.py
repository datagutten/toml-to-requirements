import pytest
from toml_to_requirements.convert_toml_to_requirements import (
    convert_toml_to_requirements,
)


def test_basic_conversion():
    toml_dict = {
        "project": {
            "dependencies": ["requests", "flask"],
        },
    }
    expected_output = "flask\nrequests"
    assert (
        convert_toml_to_requirements(
            toml_dict, include_optional=False, optional_lists=None
        )
        == expected_output
    )


def test_including_optional_dependencies():
    toml_dict = {
        "project": {
            "dependencies": ["requests"],
            "optional-dependencies": {
                "dev": ["pytest", "black"],
            },
        },
    }
    expected_output = "black\npytest\nrequests"
    assert (
        convert_toml_to_requirements(
            toml_dict, include_optional=True, optional_lists=["dev"]
        )
        == expected_output
    )


def test_excluding_unspecified_optional_dependencies():
    toml_dict = {
        "project": {
            "dependencies": ["requests"],
            "optional-dependencies": {
                "dev": ["pytest", "black"],
                "test": ["nose"],
            },
        },
    }
    expected_output = "black\npytest\nrequests"
    assert (
        convert_toml_to_requirements(
            toml_dict, include_optional=True, optional_lists=["dev"]
        )
        == expected_output
    )


def test_missing_project_section():
    toml_dict = {
        "build-system": {
            "requires": ["setuptools", "wheel"],
        },
    }
    with pytest.raises(RuntimeError) as exc_info:
        convert_toml_to_requirements(
            toml_dict, include_optional=False, optional_lists=None
        )
    assert "project section is missing" in str(exc_info.value)


def test_empty_inputs():
    toml_dict = {
        "project": {},
    }
    expected_output = ""
    assert (
        convert_toml_to_requirements(
            toml_dict, include_optional=False, optional_lists=None
        )
        == expected_output
    )
