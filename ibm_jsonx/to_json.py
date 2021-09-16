from enum import Enum

from ibm_jsonx.from_json import array
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from typing import Literal, Union, List

__all__ = ["convert"]


class JsonxTypes(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    NULL = "null"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"


def __get_all_of_type(root: Element, dt: JsonxTypes) -> list:
    base = "{http://www.ibm.com/xmlns/prod/2009/jsonx}"
    return root.findall(f"{base}{dt.value}")


def convert(data: str) -> str:
    root = ElementTree.fromstring(data)
    print(root)

    all_arrays = __get_all_of_type(root, JsonxTypes.ARRAY)
    all_booleans = __get_all_of_type(root, JsonxTypes.BOOLEAN)
    all_nulls = __get_all_of_type(root, JsonxTypes.NULL)
    all_numbers = __get_all_of_type(root, JsonxTypes.NUMBER)
    all_objects = __get_all_of_type(root, JsonxTypes.OBJECT)
    all_strings = __get_all_of_type(root, JsonxTypes.STRING)

    return ""
