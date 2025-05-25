DELETE /boards

PUT /boards
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      }
    }
  }
}

POST /boards/_doc
{
  "title": "elasticsearch 사용법"
}

GET /boards/_search
{
  "query": {
    "match": {
      "title": {
        "query": "elasiksearch",
        "fuzziness": "AUTO"
      }
    }
  }
}