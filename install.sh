#!/bin/bash
#
# usage: ./install.sh [VENV_PATH]
#
# VENV_PATH: Optional path for the virtual environment (default: ./.venv).
#
# Creates a virtualenv with uv and installs the package with test dependencies.

set -euo pipefail

VENV_PATH="${1:-.venv}"

if [ ! -d "${VENV_PATH}" ]; then
    uv venv "${VENV_PATH}"
fi

# shellcheck disable=SC1091
source "${VENV_PATH}/bin/activate"
uv pip install -e ".[tests]"
