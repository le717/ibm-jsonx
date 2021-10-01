from io import BytesIO
from typing import Callable, Optional, Type, Union
from xml.etree.ElementTree import Element, ElementTree, SubElement
from warnings import warn

from ibm_jsonx.exceptions import JsonxParsingException


__all__ = ["convert"]


def root(root_type: Union[Type[list], Type[dict]]) -> Element:
    """Create the root XML element."""
    root_tag = "object" if root_type == dict else "array"
    return Element(
        f"json:{root_tag}",
        {
            "xsi:schemaLocation": "http://www.datapower.com/schemas/json jsonx.xsd",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "xmlns:json": "http://www.ibm.com/xmlns/prod/2009/jsonx",
        },
    )


def array(root: Element, key: Optional[str], val: list) -> Element:
    """Convert a list value."""
    sub_root = SubElement(root, "json:array")

    # A "name" attribute is optional
    if key is not None:
        sub_root.attrib = {"name": key}

    # Convert all list value sub-types
    for v in val:
        converter = __get_converter(v)
        converter(sub_root, None, v)
    return root


def dictionary(root: Element, key: Optional[str], val: dict) -> Element:
    """Convert an object value."""
    sub_root = SubElement(root, "json:object")

    # A "name" attribute is optional
    if key is not None:
        sub_root.attrib = {"name": key}

    # Convert all dict key/value sub-types
    for k, v in val.items():
        converter = __get_converter(v)
        converter(sub_root, k, v)
    return root


def boolean(root: Element, key: Optional[str], val: bool) -> Element:
    """Convert a Boolean value."""
    e = SubElement(root, "json:boolean")

    # A "name" attribute is optional
    if key is not None:
        e.attrib = {"name": key}

    e.text = str(val).lower()
    return root


def special(val: str) -> str:
    """Convert special string values."""
    warn("Special character encoding is not available.", RuntimeWarning)
    return val


def string(root: Element, key: Optional[str], val: str) -> Element:
    """Convert a string value."""
    e = SubElement(root, "json:string")

    # A "name" attribute is optional
    if key is not None:
        e.attrib = {"name": special(key)}

    e.text = val
    return root


def number(root: Element, key: Optional[str], val: Union[int, float]) -> Element:
    """Convert a number value."""
    e = SubElement(root, "json:number")

    # A "name" attribute is optional
    if key is not None:
        e.attrib = {"name": key}

    e.text = str(val)
    return root


def null(root: Element, key: Optional[str], val: None) -> Element:
    """Convert a null value."""
    e = SubElement(root, "json:null")

    # A "name" attribute is optional
    if key is not None:
        e.attrib = {"name": key}

    return root


def finalize(root: Element) -> str:
    """Create a finalized XML string."""
    # The correct XML declaration header is not generated, so add it ourselves
    f = BytesIO()
    f.write(b'<?xml version="1.0" encoding="UTF-8"?>')
    ElementTree(root).write(f, encoding="UTF-8", method="xml")

    # We want a str value, not bytes
    return f.getvalue().decode("utf-8")


CONVERTERS: dict[str, Callable] = {
    "list": array,
    "dict": dictionary,
    "bool": boolean,
    "str": string,
    "float": number,
    "int": number,
    "NoneType": null,
}


def __get_converter(text: str) -> Callable:
    """Get the proper converter for this data type."""
    text_type = str(type(text)).lstrip("<class ").rstrip(">").replace("'", "")
    if text_type not in CONVERTERS:
        raise JsonxParsingException(f"Type `{text_type}` cannot be handled.")
    return CONVERTERS[text_type]


def convert(data: Union[dict, list]) -> str:
    """Convert JSON data to JSONx data."""
    # Only list and dict root elements are supported
    root_data_type = type(data)

    # if root_data_type not in (dict, list):
    if root_data_type not in (dict, list):
        raise JsonxParsingException(
            "Only `dict` and `list` root elements are supported."
        )

    # Create a root XML element
    root_element = root(root_data_type)

    # Iterate over the data correctly, depending on the root type
    # The root element is a dict
    if root_data_type == dict:
        for k, v in data.items():  # type: ignore
            converter = __get_converter(v)
            converter(root_element, k, v)

    # The root element is a list
    else:
        for v in data:
            converter = __get_converter(v)
            converter(root_element, None, v)

    # Complete the XML generation
    return finalize(root_element)
