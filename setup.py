import os
from pathlib import Path
from typing import Any, Optional, Sequence, Union

import setuptools

_PathLike = Union[str, bytes, "os.PathLike[Any]"]
_PathLikes = Sequence[_PathLike]


def _update_submodule(
    submodule_path: _PathLike,
    git_submodule_update_options: Sequence[str] = ("--init", "--depth", "1", "--"),
    working_directory_path: Optional[_PathLike] = None,
) -> None:
    import subprocess

    if (Path(str(working_directory_path) if working_directory_path else ".") / str(submodule_path) / ".git").exists():
        return

    if (
        subprocess.call(
            command := (("git", "submodule", "update") + tuple(git_submodule_update_options) + (str(submodule_path),)),
            cwd=working_directory_path,
        )
        != 0
    ):
        raise Exception(f"error: {command} failed")


def _protoc(*args: str) -> None:
    import grpc_tools
    from grpc_tools import protoc

    if (
        protoc.main(
            command := (
                "grpc_tools.protoc",
                "--proto_path={}".format(Path(grpc_tools.__file__).parent / "_proto"),
            )
            + args
        )
        != 0
    ):
        raise Exception(f"error: {command} failed")


def _build_package_grpc_protos(
    proto_paths: _PathLikes,
    import_directory_paths: Optional[_PathLikes] = None,
) -> None:
    _protoc(
        *(f"--proto_path={str(import_directory_path)}" for import_directory_path in import_directory_paths or ()),
        "--grpc_python_out=.",
        *(str(proto_path) for proto_path in proto_paths),
    )


def _build_package_protos(
    proto_paths: _PathLikes,
    import_directory_paths: Optional[_PathLikes] = None,
) -> None:
    _protoc(
        *(f"--proto_path={str(import_directory_path)}" for import_directory_path in import_directory_paths or ()),
        "--python_out=.",
        *(str(proto_path) for proto_path in proto_paths),
    )


_update_submodule("./submodules/asr-api")
_build_package_protos(
    (
        "./submodules/asr-api/proto/google/rpc/status.proto",
        "./submodules/asr-api/proto/techmo/api/status.proto",
        "./submodules/asr-api/proto/techmo/asr/api/dictation/asr.proto",
        "./submodules/asr-api/proto/techmo/asr/api/v1/asr.proto",
        "./submodules/asr-api/proto/techmo/asr/api/v1p1/asr.proto",
    ),
    import_directory_paths=("./submodules/asr-api/proto",),
)
_build_package_grpc_protos(
    (
        "./submodules/asr-api/proto/techmo/asr/api/dictation/asr.proto",
        "./submodules/asr-api/proto/techmo/asr/api/v1/asr.proto",
        "./submodules/asr-api/proto/techmo/asr/api/v1p1/asr.proto",
    ),
    import_directory_paths=("./submodules/asr-api/proto",),
)

setuptools.setup()
