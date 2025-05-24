from dataclasses import dataclass
from elasticsearch import Elasticsearch

@dataclass
class UserDocument:
    id: str # id
    name: str # fieldType.keyword
    age: int # fieldType.long
    is_active: bool # fieldType.boolean

def main():
    client = Elasticsearch(
        "http://localhost:9200",
        api_key="api_key",
    )

    if not client:
        raise Exception("Elasticsearch client not initialized")

    try:
        info = client.info()
        print(info)
    finally:
        client.close()

if __name__ == "__main__":
    main()