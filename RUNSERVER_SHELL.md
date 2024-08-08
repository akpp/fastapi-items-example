
## Run app via shell


### Run MySQL container: Option 1
```shell
docker run --rm -d \
    --name fastapi-items-example-db \
    -p 3306:3306 \
    -v fastapi-items-example_db_data:/var/lib/mysql \
    -e MYSQL_DATABASE=fastapi_items \
    -e MYSQL_ROOT_PASSWORD=rootpassword \
    -e MYSQL_USER=user \
    -e MYSQL_PASSWORD=password \
    --network fastapi-items-example --network-alias db \
    mysql:8.0 
```

#### Stop container
```shell
docker stop fastapi-items-example-db
```

### Run MySQL Docker Compose container: Option 2
```shell
docker compose up db -d
```

#### Stop container
```shell
docker compose down db
```


### Run web server
```shell
uvicorn api.main:app --reload
```