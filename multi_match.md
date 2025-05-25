DELETE /boards

PUT /boards
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "nori"
      },
      "content": {
        "type": "text",
        "analyzer": "nori"
      }
    }
  }
}

POST /boards/_doc
{
  "title": "엘라스틱서치 적용 후기",
  "content": "회사 프로덕트에 엘라스틱 서치를 적용한 후기를 공유합니다"
}

POST /boards/_doc
{
  "title": "엘라스틱서치를 사용해보니",
  "content": "검색 엔진 도입 후 성능이 향상되었습니다."
}

POST /boards/_doc
{
  "title": "검색엔진 도입 사례",
  "content": "이번 프로젝트에 엘라스틱서치를 적용한 후 많은 개선 효과가 있었습니다"
}

POST /boards/_doc
{
  "title": "레디스 캐시 사용기",
  "content": "서비스 속도 개선을 위해 캐시 시스템을 사용했습니다."
}

GET /boards/_search
{
  "query": {
    "multi_match": {
      "query": "엘라스틱 서치 적용 후기",
      "fields": [
        "title",
        "content"
      ]
    }
  }
}