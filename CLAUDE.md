# CLAUDE.md — asr-api-python

> Repo-specific guidance for AI coding agents. Inherits global conventions
> (no Claude attribution in commits; never commit generated `*_pb2.py`,
> `*_pb2_grpc.py`).

## What this is

Public Python distribution of Techmo ASR's gRPC stubs. Distributed on PyPI
as `techmo-asr-api`. Wraps proto files (vendored in `proto/`) into a
ready-to-import package with version-aliased modules (`asr_api.v1`,
`asr_api.v1p1`, `asr_api.dictation`).

## Stack and entry points

- Python ≥3.8.
- gRPC stubs generated from `proto/` at install time via `setup.py`.
- `asr_api/__init__.py` — package init.
- `asr_api/v1.py`, `v1p1.py`, `dictation.py` — version alias modules
  (re-export the generated `techmo.asr.api.<version>` namespace).
- `asr_api/VERSION.py` — single-source version (consumed by `pyproject.toml`).
- `setup.py` — runs `grpc_tools.protoc` on the proto list at build time
  (`build_package_protos` for `--python_out`, `build_package_grpc_protos`
  for `--grpc_python_out`).

## Setup vs install

This repo does **not** follow the techmo `setup.sh` / `install.sh` split —
it has no scripts at all. Per `README.md`, install with stock pip:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --require-virtualenv --upgrade pip
pip install --require-virtualenv .
```

If you need to use `uv` for parity with internal repos, the equivalent is:

```bash
uv venv .venv && source .venv/bin/activate
uv pip install -e .
```

The `pip install` step triggers `setup.py`, which calls `grpc_tools.protoc`
to generate the `*_pb2.py` / `*_pb2_grpc.py` files into the `google/` and
`techmo/` package trees.

## Generated files — never commit

The `.gitignore` explicitly excludes `google/` and `techmo/` precisely
because they are populated at install time. If `git status` shows changes
under those paths, do NOT stage them — re-run `pip install` and rely on
the local venv. The global protoc-output rule applies in full.

The proto sources themselves (`proto/google/rpc/status.proto`,
`proto/techmo/api/status.proto`, `proto/techmo/asr/api/.../asr.proto`) ARE
git-tracked — those are the inputs.

## Dependency pins (load-bearing)

- `grpcio-tools>=1.49.4,<1.63` — caps protobuf 5; raising the upper bound
  breaks the protobuf-4 compatibility this package ships under.
- `grpcio>=1.49.4,<1.63`
- `protobuf>=4.21.3,<5`

Don't relax without coordinating with downstream services that pin against
this package.

## Build / test / lint / run

This repo defines no test, lint, or run commands of its own.

- Build/install: `pip install .` (triggers proto compile).
- Smoke test: after install, `python -c "from asr_api import v1p1 as api; assert hasattr(api, 'StreamingRecognizeRequest')"`.
- No `Makefile`, no `pytest`, no `.github/workflows`, no `.gitlab-ci.yml`.

## Repo-specific gotchas

- **`submodules/asr-api/` directory is not a git submodule** in this repo.
  There is no `.gitmodules`. The proto files are vendored directly under
  `proto/`. If `submodules/asr-api/` exists in your working tree, it's a
  local artefact (likely from a sibling internal repo's setup) and is safe
  to ignore.
- Versioned modules (`v1`, `v1p1`, `dictation`) are kept as separate aliases.
  Adding a `v1p2` means: drop a new `proto/techmo/asr/api/v1p2/asr.proto`,
  add it to the two `protos_paths` lists in `setup.py`, and create an
  `asr_api/v1p2.py` alias mirroring `v1p1.py`.

## Related repos

- `github.com/techmo-pl/asr-api` — proto definitions (this repo vendors a
  copy under `proto/`).
- `github.com/techmo-pl/asr-client-python` — higher-level ASR client built
  on top of this package.
- `gitlab.devtechmo.pl/asr-team/asr-api-python` — internal mirror.

## Sections intentionally omitted

- **`setup.sh` / `install.sh`** — repo doesn't have them; uses stock pip.
- **CI** — none.
- **Tests / lint** — none defined.
