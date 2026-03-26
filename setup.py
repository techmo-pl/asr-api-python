import os
from pathlib import Path
from typing import Any, Optional, Sequence, Union

import setuptools

_PathLike = Union[str, bytes, "os.PathLike[Any]"]
_PathLikes = Sequence[_PathLike]


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


_build_package_protos(
    (
        "./proto/google/rpc/status.proto",
        "./proto/techmo/api/status.proto",
        "./proto/techmo/asr/api/dictation/asr.proto",
        "./proto/techmo/asr/api/v1/asr.proto",
        "./proto/techmo/asr/api/v1p1/asr.proto",
    ),
    import_directory_paths=("./proto",),
)
_build_package_grpc_protos(
    (
        "./proto/techmo/asr/api/dictation/asr.proto",
        "./proto/techmo/asr/api/v1/asr.proto",
        "./proto/techmo/asr/api/v1p1/asr.proto",
    ),
    import_directory_paths=("./proto",),
)

setuptools.setup()
