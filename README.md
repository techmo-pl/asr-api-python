# ASR API (Python)

The collection of gRPC APIs for Techmo ASR supplied as a Python package.

## Setup

The project can be used as-is and does not require any additional setup.

## Requirements

- [Python](https://www.python.org/) >=3.8

## Installation

### Virtual environment

Example:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --require-virtualenv --upgrade pip
pip install --require-virtualenv .
```

## Usage

### Import

The package provides a precompiled collection of `.proto` files that can be imported directly or through the alias modules.

Example:

- import from an alias module

```python
>>> from asr_api import v1p1 as api
>>> hasattr(api, "StreamingRecognizeRequest")
True
```

### Invoke RPC

Invoking RPC simply requires to call a desired method on a [_stub_](https://grpc.io/docs/what-is-grpc/core-concepts/#using-the-api) object dedicated to a specific _service_.

Example:

```python
import wave

import grpc
from asr_api import v1p1 as api

# This example assumes that the endpoint is an instance
# of techmo.asr.api.v1p1.Asr service listening on the local 30384 port.
grpc_service_address = "127.0.0.1:30384"

# Audio data come from a mono 16-bit linear PCM encoded WAV file.
audio_file = wave.open("audio.wav", "rb")
audio_bytes = audio_file.readframes(audio_file.getnframes())
audio_sampling_rate_hz = audio_file.getframerate()

with grpc.insecure_channel(grpc_service_address) as grpc_channel:
    asr_stub = api.AsrStub(grpc_channel)

    requests = (
        api.StreamingRecognizeRequest(
            config=api.StreamingRecognizeRequestConfig(
                audio_config=api.AudioConfig(
                    encoding=api.AudioConfig.AudioEncoding.LINEAR16,
                    sampling_rate_hz=audio_sampling_rate_hz,
                ),
                speech_recognition_config=api.SpeechRecognitionConfig(
                    enable_speech_recognition=True,
                ),
            ),
        ),
        api.StreamingRecognizeRequest(
            data=api.StreamingRecognizeRequestData(
                audio=api.Audio(bytes=audio_bytes),
            ),
        ),
    )

    for response in asr_stub.StreamingRecognize(iter(requests)):
        print(response)
```

#### Note about audio bytes and samples

Even though samples are easier to work with, finally audio must be sent in its pure binary representation, not decoded as samples. To encode samples into bytes, the [_struct_](https://docs.python.org/3/library/struct.html#module-struct) Python module comes in handy.

```python
import struct

# Imagine that audio samples are an array of integers
# (mono signed little-endian 16-bit linear PCM encoded samples in this case).
audio_samples = []
audio_bytes = struct.pack(f"<{len(audio_samples)}h", *audio_samples)
```
