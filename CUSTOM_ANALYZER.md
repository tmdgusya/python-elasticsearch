product 라는 인덱스 만들때 애널라이저를 커스텀 하기 위해서는 아래와 같이 설정해주면 된다. (**으음**, 요거 한국어 애널라이저 좋은거 쓰면 우리거 검색 순위 높일 수 있겠는데)
```sh
PUT /products

{
    "settings": {
        "analysis": {
            "analyzer": {
                "products_name_analyzer": {
                    "char_filter": [],
                    "tokenizer": "standard",
                    "filter": []
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
위와 같이 lowercase filter 를 설정안했을때는 아래 케이스가 검색이 안됨. 왜? Apple 이 lowercase 로 등록이 안됬기 때문임.
```sh
POST /products/_create/1
{
    "name": "Apple 2025 맥북 에어 13 M4 10코어"
}

# apple 로 검색할때는 아무것도 안나옴, 그 이유는 Lowercase 가 적용안됬기 때문임
GET /products/_search
{
    "query": {
        "match": {
            "name": "Apple"
        }
    }
}
```
```sh
GET /products/_analyze

{
    "field": "name",
    "text": "Apple 2025 맥북 에어 13 M4 10코어"
}

{
  "tokens": [
    {
      "token": "Apple",
      "start_offset": 0,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "2025",
      "start_offset": 6,
      "end_offset": 10,
      "type": "<NUM>",
      "position": 1
    },
    {
      "token": "맥북",
      "start_offset": 11,
      "end_offset": 13,
      "type": "<HANGUL>",
      "position": 2
    },
    {
      "token": "에어",
      "start_offset": 14,
      "end_offset": 16,
      "type": "<HANGUL>",
      "position": 3
    },
    {
      "token": "13",
      "start_offset": 17,
      "end_offset": 19,
      "type": "<NUM>",
      "position": 4
    },
    {
      "token": "M4",
      "start_offset": 20,
      "end_offset": 22,
      "type": "<ALPHANUM>",
      "position": 5
    },
    {
      "token": "10코어",
      "start_offset": 23,
      "end_offset": 27,
      "type": "<ALPHANUM>",
      "position": 6
    }
  ]
}
```
만약 제대로된 검색결과가 나오려면 이렇게 해야함 `"filter": ["lowercase"]`
