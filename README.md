## Elastic Search

9200 port 를 통해 REST API를 통해 데이터를 추가하고 검색할 수 있습니다.

### REST API

```sh
curl -X POST "localhost:9200/users/_doc" -H "Content-Type: application/json" -
{
  "name" : "Alice",
  "email" : "alice@example.com"
}
```

###

```sql
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
```