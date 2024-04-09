from __future__ import annotations
from typing import Any


def convert_toml_to_requirements(
    parsed_toml_file: dict[str, Any],
    *,
    include_optional: bool,
    optional_lists: list[str] | None,
) -> str:
    project: Any | None = parsed_toml_file.get("project")

    if project is None:
        raise RuntimeError(
            "The project section is missing from the TOML file. Exiting..."
        )

    dependencies = set(project.get("dependencies", []))

    if include_optional:
        optional_dependency_list: dict[str, Any] = project.get(
            "optional-dependencies", {}
        )
        # Use a set for efficient inclusion checks
        optional_lists_to_include: set[str] = (
            set(optional_lists) if optional_lists is not None else set()
        )

        for optional_list, deps in optional_dependency_list.items():
            if (
                optional_lists_to_include
                and optional_list not in optional_lists_to_include
            ):
                continue

            dependencies.update(deps)

    return "\n".join(sorted(dependencies))
