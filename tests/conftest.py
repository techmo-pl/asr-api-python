from typing import List

import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--api",
        default=None,
        choices=[
            "techmo.asr.api.dictation",
            "techmo.asr.api.v1",
            "techmo.asr.api.v1p1",
        ],
        help="the argument of tests marked with the `@pytest.mark.api(name)` marker to be collected; one of: %(choices)s (default is %(default)r)",
        metavar="name",
    )


def pytest_collection_modifyitems(config: pytest.Config, items: List[pytest.Item]) -> None:
    if api := config.getoption("--api"):
        items[:] = (item for item in items if (mark := item.get_closest_marker("api")) and mark.args and mark.args[0] == api)
