# TOML to Requirements

Simple script to convert a pyproject.toml file to a requirements.txt file.

Does not support poetry projects! They have their own converter tools.

## Installation

Install with pip:

```bash
pip install toml-to-requirements
```

## Usage

### Basic

Run the following command to generate a requirements.txt file without including optional dependencies:

```bash
toml-to-req --toml-file pyproject.toml
```

### Optional Dependencies

To include optional dependencies, include the `--optional-lists` flag in the above command:

```bash
toml-to-req --toml-file pyproject.toml --optional-lists dev,test
```

### Poetry

To convert a poetry project, run the following command:

```bash
toml-to-req --toml-file pyproject.toml --poetry
```

## License

MIT
