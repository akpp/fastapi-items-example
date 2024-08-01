
## Run app via Docker

TODO: Debugger [FastAPI-Items-Docker](.run/FastApi-Items-Docker.run.xml) doesn't work!


### Run web server
```shell
uvicorn api.main:app --reload
```

### Create the network
```
docker network create fastapi-items-example
```


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

### Run the App
Build an image
```shell
docker build -t fastapi-items-example .
```

```shell
docker run --rm \
    --name fastapi-items-example-web \
    --network fastapi-items-example \
    -e MYSQL_HOST=db \
    -p 8000:8000 \
    fastapi-items-example
```

#### Stop container
```shell
docker stop fastapi-items-example-web
```