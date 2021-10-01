from enum import Enum
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, ParseError
from typing import Callable, NoReturn, Union
from warnings import warn

from ibm_jsonx.exceptions import JsonxParsingException


__all__ = ["convert"]


class JsonxTypes(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    NULL = "null"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"


def array(ele: Element) -> list:
    """Convert to a list object."""
    final = []

    for v in ele:
        converter = __get_converter(__get_type(v.tag).value)
        final.append(converter(v))
    return final


def dictionary(ele: Element) -> dict:
    """Convert to a dictionary object."""
    final = {}

    for v in ele:
        converter = __get_converter(__get_type(v.tag).value)
        final[v.attrib["name"]] = converter(v)
    return final


def boolean(val: Element) -> bool:
    """Convert to a Boolean value."""
    return True if val.text == "true" else False


def string(ele: Element) -> str:
    """Convert to a string value."""
    return special(ele.text) if ele.text else ""


def special(text: str) -> str:
    """Convert special string values."""
    warn("Special character encoding is not available.", RuntimeWarning)
    return text


def number(ele: Element) -> Union[float, int]:
    """Convert to a float/into value."""
    # This _should_ have a value
    if ele.text is None:
        raise JsonxParsingException("Type `number` must have a value")

    try:
        return int(ele.text)
    except ValueError:
        return float(ele.text)


def null(val: Element) -> None:
    """Convert to a None value."""
    return None


CONVERTERS: dict[str, Callable] = {
    "array": array,
    "object": dictionary,
    "boolean": boolean,
    "string": string,
    "number": number,
    "null": null,
}


def __get_converter(type: str) -> Callable:
    """Get the proper converter for this data type."""
    if type not in CONVERTERS:
        raise JsonxParsingException(f"Type `{type}` cannot be handled.")
    return CONVERTERS[type]


def __get_type(tag: str) -> JsonxTypes:
    """Determine the data type of this element."""
    return JsonxTypes(tag[tag.find("}") + 1 :])


def __get_root_element(type: JsonxTypes) -> Union[dict, list, NoReturn]:
    """Determine the root JSON element."""
    if type is JsonxTypes.OBJECT:
        return {}
    elif type is JsonxTypes.ARRAY:
        return []
    else:
        raise JsonxParsingException(
            "Only `dict` and `list` root elements are supported."
        )


def convert(data: str) -> Union[dict, list]:
    """Convert JSONx data to JSON data."""
    # Parse the XML into a data structure we can use
    try:
        root = ElementTree.fromstring(data)
    except ParseError as exc:
        raise JsonxParsingException(exc.msg)

    # Create the root container element
    root_element = __get_root_element(__get_type(root.tag))

    # Go through the XML tree and convert the data
    for child in root:
        converter = __get_converter(__get_type(child.tag).value)
        converted_value = converter(child)

        # Build up the final data based on the root container type
        if type(root_element) == dict:
            root_element[child.attrib["name"]] = converted_value
        elif type(root_element) == list:
            root_element.append(converted_value)

    return root_element
