import json
from pathlib import Path
from typing import Union

from ibm_jsonx import from_json, to_json


__all__ = ["from_jsonx", "to_jsonx", "file_from_jsonx", "file_to_jsonx"]


def from_jsonx(data: str) -> str:
    """Convert JSONx to stringified JSON."""
    return json.dumps(to_json.convert(data))


def to_jsonx(data: str) -> str:
    """Convert stringified JSON to JSONx."""
    return from_json.convert(json.loads(data))


def file_to_jsonx(file_name: Union[str, Path]) -> str:
    """Convert a JSON file to JSONx data."""
    # Handle a non-PathLike argument
    if not isinstance(file_name, Path):
        file_name = Path(file_name).resolve()
    return to_jsonx(file_name.read_text())


def file_from_jsonx(file_name: Union[str, Path]) -> str:
    """Convert a JSONx file to stringified JSON data."""
    # Handle a non-PathLike argument
    if not isinstance(file_name, Path):
        file_name = Path(file_name).resolve()
    return from_jsonx(file_name.read_text())
