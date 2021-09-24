import json
from pathlib import Path
from typing import Union

from ibm_jsonx import from_json, to_json


__all__ = ["from_jsonx", "to_jsonx"]


def from_jsonx(data: Union[str, Path], outfile: Path = None) -> str:
    """Convert JSONx to stringified JSON."""
    # If we got a PathLike instance as the input, get the text from it
    if isinstance(data, Path):
        data = data.read_text()

    # Convert the data
    json_data = json.dumps(to_json.convert(data))

    # We were asked to output it to a file, so do that
    if outfile:
        outfile.write_text(json_data)

    # Always return the data regardless
    return json_data


def to_jsonx(data: Union[str, Path], outfile: Path = None) -> str:
    """Convert stringified JSON to JSONx."""
    # If we got a PathLike instance as the input, get the text from it
    if isinstance(data, Path):
        data = data.read_text()

    jsonx_data = from_json.convert(json.loads(data))

    # We were asked to output it to a file, so do that
    if outfile:
        outfile.write_text(jsonx_data)

    # Always return the data regardless
    return jsonx_data
