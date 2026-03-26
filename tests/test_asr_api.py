from typing import cast

import pytest


@pytest.fixture
def asr_api_dictation() -> object:
    import asr_api.dictation

    return asr_api.dictation


@pytest.fixture(
    params=(
        "Speech",
        "RecognizeRequest",
        "StreamingRecognizeRequest",
        "StreamingRecognitionConfig",
        "RecognitionConfig",
        "SpeechDurationConfig",
        "SpeechDurationThresholdMode",
        "SpeechContext",
        "ConfigField",
        "RecognitionAudio",
        "RecognizeResponse",
        "StreamingRecognizeResponse",
        "StreamingRecognitionResult",
        "SpeechRecognitionResult",
        "SpeechRecognitionAlternative",
        "WordInfo",
        "RecognitionLattice",
        "LatticeEdge",
        "Gender",
        "Age",
    ),
)
def asr_api_dictation_attr(request: pytest.FixtureRequest) -> str:
    return cast(str, request.param)


@pytest.fixture
def asr_api_v1() -> object:
    import asr_api.v1

    return asr_api.v1


@pytest.fixture(
    params=(
        "Asr",
        "StreamingRecognizeRequest",
        "StreamingRecognizeRequestConfig",
        "ResultConfig",
        "StreamingConfig",
        "AudioConfig",
        "AgeRecognitionConfig",
        "GenderRecognitionConfig",
        "LanguageRecognitionConfig",
        "SpeechRecognitionConfig",
        "StreamingRecognizeRequestControlMessage",
        "StreamingRecognizeRequestData",
        "Audio",
        "StreamingRecognizeResponse",
        "StreamingRecognizeResult",
        "AgeRecognitionResult",
        "AgeRecognitionAlternative",
        "GenderRecognitionResult",
        "GenderRecognitionAlternative",
        "LanguageRecognitionResult",
        "LanguageRecognitionAlternative",
        "SpeechRecognitionResult",
        "SpeechRecognitionAlternative",
        "SpeechRecognitionWord",
    ),
)
def asr_api_v1_attr(request: pytest.FixtureRequest) -> str:
    return cast(str, request.param)


@pytest.fixture
def asr_api_v1p1() -> object:
    import asr_api.v1p1

    return asr_api.v1p1


@pytest.fixture(
    params=(
        "Asr",
        "StreamingRecognizeRequest",
        "StreamingRecognizeRequestConfig",
        "ResultConfig",
        "StreamingConfig",
        "AudioConfig",
        "AgeRecognitionConfig",
        "GenderRecognitionConfig",
        "LanguageRecognitionConfig",
        "SpeechRecognitionConfig",
        "StreamingRecognizeRequestControlMessage",
        "StreamingRecognizeRequestData",
        "Audio",
        "StreamingRecognizeResponse",
        "StreamingRecognizeResult",
        "AgeRecognitionResult",
        "AgeRecognitionAlternative",
        "GenderRecognitionResult",
        "GenderRecognitionAlternative",
        "LanguageRecognitionResult",
        "LanguageRecognitionAlternative",
        "SpeechRecognitionResult",
        "SpeechRecognitionAlternative",
        "SpeechRecognitionWord",
    ),
)
def asr_api_v1p1_attr(request: pytest.FixtureRequest) -> str:
    return cast(str, request.param)


@pytest.mark.parametrize(
    "api, attr",
    (
        pytest.param(
            pytest.lazy_fixture("asr_api_dictation"),
            pytest.lazy_fixture("asr_api_dictation_attr"),
            marks=pytest.mark.api("techmo.asr.api.dictation"),
        ),
        pytest.param(
            pytest.lazy_fixture("asr_api_v1"),
            pytest.lazy_fixture("asr_api_v1_attr"),
            marks=pytest.mark.api("techmo.asr.api.v1"),
        ),
        pytest.param(
            pytest.lazy_fixture("asr_api_v1p1"),
            pytest.lazy_fixture("asr_api_v1p1_attr"),
            marks=pytest.mark.api("techmo.asr.api.v1p1"),
        ),
    ),
)
def test_hasattr(api: object, attr: str) -> None:
    assert hasattr(api, attr)
