## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "messge": " Descrition of what happend"
}
```

Subsecuent response definitions will only detail the expected vaule of the `data field`

###List all responses

**Definition**

`GET /decision`

**Response**

- `200 OK` on success

``` json
[
    {
        "id": "Consults_20/02/2020",
        "document": "VGVzdCx0ZXN0MSx0ZXN0MiAwLDEsMg=="
    }
]
```

