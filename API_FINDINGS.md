# API Findings: JSONPlaceholder

Testers (pair): \<farisha>, \<hakim>  
Date: 26 October 2026

Record what the server actually returned for each route. A value copied from the documentation without being checked against a real request is not a finding.

## GET /posts/1

| Field | Value |
|---|---|
| Status code | 200 |
| Content-Type | application/json; charset=utf-8 |

Response body keys and their types:

| Key | Type | Example value |
|---|---|---|
| userId | Integer | 1 |
| id | Integer | 1 |
| title | String | sunt aut facere repellat provident occaecati excepturi optio reprehenderit |
| body | String | quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam |

## GET /posts

| Field | Value |
|---|---|
| Status code | 200 |
| Content-Type | application/json; charset=utf-8 |

Shape of the response body (object or array, and the type of each element):

The response body is a JSON array (Python list) containing 100 post objects. Each element is a JSON object with the keys `userId` (integer), `id` (integer), `title` (string), and `body` (string).

## POST /posts

Request body sent:

```json
{
  "title": "API testing",
  "body": "Testing POST requests",
  "userId": 1
}
```

| Field | Value |
|---|---|
| Status code | 201 |
| Content-Type | application/json; charset=utf-8 |

Response body keys and their types:

| Key | Type | Example value |
|---|---|---|
| title | String | API testing |
| body | String | Testing POST requests |
| userId | Integer | 1 |
| id | Integer | 101 |

## DELETE /posts/1

| Field | Value |
|---|---|
| Status code | 200 |
| Content-Type | application/json; charset=utf-8 |

Response body:

An empty JSON object: `{}`.

## Notes

JSONPlaceholder returned a successful response for all four requests. The GET requests retrieved one post and a list of 100 posts. The POST request returned HTTP 201 and a generated ID of 101.

The DELETE request returned HTTP 200 with an empty JSON object. JSONPlaceholder simulates write operations, so the successful response does not establish that the post was permanently deleted from the underlying dataset.
