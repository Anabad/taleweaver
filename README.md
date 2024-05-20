# Taleweaver

A simple interface to run choose your own adventure type games.

## Prerequisites

python (>=3.10)
poetry: https://python-poetry.org/docs/

## Installation

This project uses poetry as dependency manager. To install run:

```
poetry install
```
## Run

The project entrypoint is src/main.py. To run use:

```
poetry run python src/main.py
```

## Contributing

### Adding a tale

To add a new tale, simply add a yaml file following the format laid out in the **ravenloft_echoes.yaml** file to the tales directory.

Each tale must contain the following elements:
- A **title**
- A set of **nodes** following these constraints:
    - Each node should have a **title**, **text**, and **choices** field
    - A start node with the key **"start"**
    - At least one ending node where **choices** is an empty dict

### Contrbuting to the code

Contributing to the code is done via pull request

Your pull request should adhere to the following standards:

- All commit messages should use the conventionnal commit format: https://www.conventionalcommits.org/en/v1.0.0/
- Code should be properly linted and formatted using the project's ruff configuration
- Code should be properly typed using the project's mypy configuration
- New code should be tested with pytest

A pre-commit configuration is provided to help run ruff and mypy automatically to install, run `pre-commit install` from the project virtualenv.

Happy weaving!
