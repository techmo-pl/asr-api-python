# Changelog of ASR API (Python)


## [1.1.4] - 2026-03-22 (#25)

### Added

- documentation
  - `CLAUDE.md` with verified development context for AI-assisted sessions

### Fixed

- ci
  - `test` and `test_py314` jobs: added `export PATH="$HOME/.local/bin:$PATH"` before `./install.sh` so that `uv` is found on runners where it is installed locally rather than system-wide
- version
  - `VERSION.py` was not updated when 1.1.3 was tagged; corrected now

### Changed

- submodules
  - `asr-api` updated to v1.1.1 (adds `CLAUDE.md` to proto definitions repo)


## [1.1.3] - 2026-03-04

### Changed

- build
  - replaced `pkg_resources` with importlib-compatible path resolution in `setup.py`
  - removed upper bound on setuptools (no longer required without `pkg_resources`)
  - removed upper bound on grpcio-tools build requirement
  - replaced `submodules/pre-commit` git submodule with shallow `git clone` in `setup.sh` and CI
- dependencies
  - removed upper bound on grpcio runtime requirement
  - removed upper bound on protobuf runtime requirement
  - added Python-version markers to guard Python 3.8 users from grpcio>=1.71.0 and protobuf>=6.0.0
- ci
  - introduced `tox.ini` and `install.sh` for uv-based multi-version testing (3.8–3.14)
  - replaced Docker-based single-version test with tox multi-version matrix (3.8–3.14)
  - fixed linter job to use setup.sh (was incorrectly using inline git clone)
  - removed Dockerfile and .dockerignore (CI no longer uses Docker)


## [1.1.2] - 2026-02-09 (#23)

### Changed

- dependencies
  - introduced upper bound on setuptools to lower than 82 because of drop of pkg_resources


## [1.1.1] - 2024-09-04 (#19)

### Changed

- dependencies
  - lower and upper bound on grpcio requirement to be more or equal to 1.49.4 and less than 1.63 (#19)
  - lower and upper bound on protobuf requirement to be more or equal to 4.21.3 and less than 5 (#19)
- build dependencies
  - lower and upper bound on grpcio-tools requirement to be more or equal to 1.49.4 and less than 1.63 (#19)


## [1.1.0] - 2024-04-26 (#14)

### Added

- _asr_api_ package
  - support for _techmo.asr.api.v1p1_ API (#15)
- unit tests
  - attribute check of _techmo.asr.api.v1p1_ API

### Changed

- submodules
  - asr-api (v1.1.0)


## [1.0.0] - 2024-01-29 (#8)

### Added

- _asr_api_ package
  - support for _techmo.asr.api.dictation_ API (#10)
  - support for _techmo.asr.api.v1_ API (#10)
- Setuptools configuration
- Dockerfile for development
- GitLab CI configuration
- unit tests
  - attribute check of _techmo.asr.api.dictation_ API
  - attribute check of _techmo.asr.api.v1_ API
  - coverage report
- submodules
  - asr-api (v1.0.0)
  - pre-commit (v1.3.0)
