from pathlib import Path
from typing import List

import setuptools


def protoc(args: List[str]):
    import pkg_resources
    from grpc_tools import protoc

    command = [
        "grpc_tools.protoc",
        "--proto_path={}".format(
            Path(pkg_resources.resource_filename("grpc_tools", "_proto"))
        ),
    ] + args

    if protoc.main(command) != 0:
        raise Exception("error: {} failed".format(command))


def build_package_grpc_protos(
    protos_paths: List[Path], import_directory_paths: List[Path] = []
):
    protoc(
        [
            "--proto_path={}".format(Path(import_directory_path))
            for import_directory_path in import_directory_paths
        ]
        + ["--grpc_python_out=."]
        + protos_paths,
    )


def build_package_protos(
    protos_paths: List[Path], import_directory_paths: List[Path] = []
):
    protoc(
        [
            "--proto_path={}".format(Path(import_directory_path))
            for import_directory_path in import_directory_paths
        ]
        + ["--python_out=."]
        + protos_paths,
    )


build_package_protos(
    protos_paths=[
        "./proto/google/rpc/status.proto",
        "./proto/techmo/api/status.proto",
        "./proto/techmo/asr/api/dictation/asr.proto",
        "./proto/techmo/asr/api/v1/asr.proto",
        "./proto/techmo/asr/api/v1p1/asr.proto",
    ],
    import_directory_paths=[
        "./proto",
    ],
)
build_package_grpc_protos(
    protos_paths=[
        "./proto/techmo/asr/api/dictation/asr.proto",
        "./proto/techmo/asr/api/v1/asr.proto",
        "./proto/techmo/asr/api/v1p1/asr.proto",
    ],
    import_directory_paths=[
        "./proto",
    ],
)

setuptools.setup()
