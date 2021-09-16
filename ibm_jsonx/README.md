# ibm_jsonx

> Convert JSON to IBM's JSONx format.

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

# Also supports loading from a PathLike object or string file path
ibm_jsonx.file_to_jsonx(pathlib.Path("json-data.json"))
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
