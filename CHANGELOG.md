# Changelog of ASR API (Python)


## [1.1.4] - 2026-03-22

### Fixed

- `install.sh`: added `export PATH="$HOME/.local/bin:$PATH"` so that `uv` is found on runners where it is installed locally rather than system-wide.
- `VERSION.py`: corrected version string (was not updated when 1.1.3 was tagged).

### Changed

- `setup.py`: replaced `pkg_resources` with importlib-compatible path resolution; removed upper bound on setuptools; removed upper bound on grpcio-tools build requirement.
- `pyproject.toml`: removed upper bound on grpcio and protobuf runtime requirements; added Python-version markers to guard Python 3.8 users from grpcio>=1.71.0 and protobuf>=6.0.0; grpcio bounds set to `>=1.49.4,<1.71.0` for Python 3.8 and `>=1.49.4` for 3.9+; protobuf bounds set to `>=4.21.3,<6`; `requires-python` lowered to `>=3.8`; introduced upper bound on setuptools below 82; added `pip<26` constraint.
- `tox.ini`, `install.sh`: introduced uv-based multi-version testing (Python 3.8–3.14); replaced Docker-based single-version test with tox multi-version matrix.
- `submodules/asr-api`: updated to v1.1.1; restructured from committed proto files to a submodule.
- `asr_api/`: support for _techmo.asr.api.v1p1_ API.
- `tests/`: attribute check for _techmo.asr.api.v1p1_ API.


## [1.0.0] - 2024-01-29

### Added

- `asr_api/`: support for _techmo.asr.api.dictation_ and _techmo.asr.api.v1_ APIs.
- `pyproject.toml`: setuptools configuration.
- `tests/`: attribute checks for _techmo.asr.api.dictation_ and _techmo.asr.api.v1_ APIs; coverage report.
- `submodules/asr-api`: asr-api v1.0.0.
