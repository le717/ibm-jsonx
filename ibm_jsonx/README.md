# ibm_jsonx

> Convert data between JSON to IBM's JSONx format.

## Rationale

Because I could.

- [JSONx documentation](https://www.ibm.com/docs/en/datapower-gateways/2018.4?topic=20-jsonx)

## Usage

Don't.

```python
import pathlib

import ibm_jsonx


json_data = """{
  "name":"John Smith",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": 10021,
  },
  "phoneNumbers": [
    "212 555-1111",
    "212 555-2222"
  ],
  "additionalInfo": null,
  "remote": false,
  "height": 62.4,
  "ficoScore": " > 640"
}"""

# Load stringified JSON data
ibm_jsonx.to_jsonx(json_data)

# Also supports loading from/to a PathLike object
ibm_jsonx.to_jsonx(pathlib.Path("json-data.json"), pathlib.Path("jsonx-data.xml"))

# Also works the other direction
ibm_jsonx.from_jsonx(pathlib.Path("jsonx-data.xml"))  # type: str
```

## Building

1. Install Python 3.9+
1. Install [Poetry](https://python-poetry.org/)
1. Run `poetry install`
1. Run `poetry build`
1. Tests can be run via the provided VS Code test runner config.

The resuting `.whl` file will be located at
`./dist/ibm_jsonx-<x.y.z>-py3-none-any.whl`

## Creation

2021 Caleb

[MIT](LICENSE)
