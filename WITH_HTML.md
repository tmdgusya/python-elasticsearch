DELETE /boards

PUT /boards
{
    "settings": {
        "analysis": {
            "analyzer": {
                "boards_content_analyzer": {
                    "char_filter": ["html_strip"],
                    "tokenizer": "standard",
                    "filter": ["lowercase"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "content": {
                "type": "text",
                "analyzer": "boards_content_analyzer"
            }
        }
    }
}

POST /boards/_doc
{
    "content": "<h1>Running cats, jumping quickly - over the lazy dogs!</h1>"
}

GET /boards/_search
{
    "query": {
        "match": {
            "content": "running"
        }
    }
}

GET /boards/_analyze
{
    "field": "content",
    "text": "<h1>Running cats, jumping quickly - over the lazy dogs!</h1>"
}