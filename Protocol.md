# SelfMsg Protocol v1


## Transport

- HTTP over local network
- JSON for request/response bodies

## Message Model

```json
{
  "id": "uuid",
  "type": "text",
  "sender": "cli",
  "timestamp": 1734512345,
  "content": "hello"
}
```

## Endpoints

1. Health Check

`GET /health`

Response

```json
{
    "status": "ok"
}
```

2. Send Messages

`POST /messages`

Request

```json
{
  "type": "text",
  "sender": "cli",
  "content": "hello"
}
```

Response

```json
{
    "id": "uuid",
    "timestamp": 21321321
}
```

3. Fetch Messages

`GET /messages`

Optional Query Params:

`GET /messages?since=123123123`

Response

```json
[
    {
        "id": "uuid",
        "type": "text",
        "sender": "android",
        "timestamp": 123123,
        "content": "something idk"
    }
]
```

## Error Format

```json
{
    "error": "invalid_req",
    "message": "Missing content field"
}
```