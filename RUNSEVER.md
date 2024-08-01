
## Run app manually
### Run web server
```shell
uvicorn api.main:app --reload
```

### Run MySQL container
```shell
docker run --rm -d \
    -p 3306:3306 \
    -v fastapi-items-example_db_data:/var/lib/mysql \
    -e MYSQL_DATABASE=fastapi_items \
    -e MYSQL_ROOT_PASSWORD=rootpassword \
    -e MYSQL_USER=user \
    -e MYSQL_PASSWORD=password \
    --name fastapi-items-example-db \
    mysql:8.0 
```

#### Stop container
```shell
docker stop fastapi-items-example-db
```

### Run MySQL Docker Compose container
```shell
docker compose up db -d
```

#### Stop container
```shell
docker compose down db
```

