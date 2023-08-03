# PDF API PYTON
This API uses `POST` request to communicate and HTTP [response codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) to indenticate response and error. All requests must include a `content-type` of `application/json` and the body must be valid JSON.

### Dependence
```pip install pdfkit```

```wkhtmltopdf```

### Response Codes
```
200: Success
500: Server Error
```

### Example Error Message
```json
http code 402
{
    "error"     : true,
    "response"  : "Message error",
}
```

**Request:**
```json
POST /pdf HTTP/1.1
Accept: application/json
Content-Type: application/json
{
    "content": "<h1>Hellow world</h1>"    
}
```
**Successful Response:**
```json
HTTP/1.1 200 OK
Server: My RESTful API
Content-Type: application/pdf
```

| Query key     | Description     |
| ------------- | --------------- |
| ```content``` | html content    |
| ```url```     | page url        |
| ```options``` | [reference](https://wkhtmltopdf.org/usage/wkhtmltopdf.txt)|
