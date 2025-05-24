```sh
PUT /products

{
    "settings": {
        "analysis": {
            "filter": {
                "products_synonym_filter": {
                    "type": "synonym",
                    "synonyms": [
                        "notebook, 노트북, 랩탑, 휴대용 컴퓨터, laptop",
                        "삼성, samsung"
                    ]
                }
            },
            "analyzer": {
                "products_name_analyzer": {
                    "char_filter": [],
                    "tokenizer": "standard",
                    "filter": [
                        "lowercase",
                        "products_synonym_filter"
                    ]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "name": {
                "type": "text",
                "analyzer": "products_name_analyzer"
            }
        }
    }
}
```

위와 같이 synonym 을 설정해둔 뒤에 아래와 같이 _analyze 를 통해 분석해보면 동의어로 역인덱스로 변경됬음을 확인해볼수 있다.
```
GET /products/_analyze
{
    "field": "name",
    "text": "랩탑"
}
```
```sh
{
  "tokens": [
    {
      "token": "랩탑",
      "start_offset": 0,
      "end_offset": 2,
      "type": "<HANGUL>",
      "position": 0
    },
    {
      "token": "notebook",
      "start_offset": 0,
      "end_offset": 2,
      "type": "SYNONYM",
      "position": 0
    },
    {
      "token": "노트북",
      "start_offset": 0,
      "end_offset": 2,
      "type": "SYNONYM",
      "position": 0
    },
    {
      "token": "휴대용",
      "start_offset": 0,
      "end_offset": 2,
      "type": "SYNONYM",
      "position": 0
    },
    {
      "token": "laptop",
      "start_offset": 0,
      "end_offset": 2,
      "type": "SYNONYM",
      "position": 0
    },
    {
      "token": "컴퓨터",
      "start_offset": 0,
      "end_offset": 2,
      "type": "SYNONYM",
      "position": 1
    }
  ]
}
```

그럼 여기서 내 질문 동의어 사전이 많아지면 쿼리할때 쿼리도 filter 를 타게 되니까 복잡도가 높아지나?