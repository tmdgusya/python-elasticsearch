DELETE /products

PUT /products
{
  "mappings": {
    "properties": {
      "name": {
        "type": "text",
        "analyzer": "nori"
      },
      "rating": {
        "type": "float"
      },
      "likes": {
        "type": "integer"
      }
    }
  }
}

POST /products/_doc
{
  "name": "무선 충전기 C 타입",
  "rating": 4.9,
  "likes": 300
}

POST /products/_doc
{
  "name": "갤럭시 버즈2 무선 이어폰",
  "rating": 5.0,
  "likes": 1000
}

POST /products/_doc
{
  "name": "소니 무선 이어폰 MF",
  "rating": 3.8,
  "likes": 15
}

POST /products/_doc
{
  "name": "삼성 노트북 13인치",
  "rating": 5.0,
  "likes": 1000
}

GET /products/_search
{
  "query": {
    "bool": {
      "must": [ // must 는 scoring 이 되기 때문임
        {
          "match": {
            "name": "무선 이어폰"
          }
        }
      ],
      "should": [
        {
          "range": {
            "rating": { // rating 이 4.5 이상일때 가산점을 부가하겠다.
              "gte": 4.5
            }
          }
        },
        {
          "range": {
            "likes": {
              "gte": 100
            }
          }
        }
      ]
    }
  }
}