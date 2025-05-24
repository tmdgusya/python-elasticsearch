DELETE /products

# 인덱스를 만들면서 mapping 까지 정의하는 방법
PUT /products
{
    "mappings": {
        "properties": {
            "name": {
                "type": "text"
            }
        }
    }
}

GET /products

POST /products/_create/1
{
    "name": "Apple 2025 맥북 에어 13 M4 10코어"
}

POST /products/_create/2
{
    "name": "Apple 2024 에어팟 4세대"
}

POST /products/_create/3
{
    "name": "Apple 2024 아이패드 mini A17 Pro"
}

GET /products/_search
{
    "query": {
        "match": {
            "name": "Apple 2024 아이패드"
        }
    }
}