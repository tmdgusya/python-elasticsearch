from dataclasses import dataclass
# from elasticsearch import Elasticsearch
from elasticsearch import AsyncElasticsearch

@dataclass
class UserDocument:
    id: str # id
    name: str # fieldType.keyword
    age: int # fieldType.long
    is_active: bool # fieldType.boolean

async def main():
    client = AsyncElasticsearch(
        "http://localhost:9200",
        api_key="api_key",
    )

    if not client:
        raise Exception("Elasticsearch client not initialized")

    try:
        info = await client.info()
        print(info)
    finally:
        await client.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())