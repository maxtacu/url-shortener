## Overview

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.8+

## Usage
To run the server locally, please execute the following from the root directory:

```
docker run --rm -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=flaskshortener mysql:5.7
pip3 install -r requirements.txt
python3 -m api_server
```

and open your browser here:

```
http://localhost:8080/ui/
```

Your API definition lives here:

```
http://localhost:8080/openapi.json
```

## Running with Docker

To run the server on a Docker container, please execute the following from the flask directory:

```bash
# building the image
docker build -t api_server .

# starting up a container
docker run -p 8080:8080 --network="host" api_server
```