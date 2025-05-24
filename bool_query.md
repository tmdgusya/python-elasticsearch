DELETE /boards

PUT /boards
{
    "mappings": {
        "properties": {
            "board_id": {
                "type": "long"
            },
            "title": {
                "type": "text",
                "analyzer": "nori"
            },
            "category": {
                "type": "keyword"
            },
            "is_notice": {
                "type": "boolean"
            },
            "created_at": {
                "type": "date"
            }
        }
    }
}

POST /boards/_doc
{
    "board_id": 1,
    "title": "엘라스틱서치는 정말 강력한 검색엔진이에요",
    "category": "자유 게시판",
    "is_notice": false,
    "created_at": "2025-05-01T12:00:00"
}

GET /boards/_search
{
    "query": {
        "bool": {
            "must": [
              {
                "match": {
                  "title": "검색엔진"
                }
              }
            ],
            "filter": [
                {
                    "term": {
                        "category": "자유 게시판"
                    }
                },
                {
                    "term": {
                      "is_notice": false
                    }
                }
            ]
        } 
    }
}