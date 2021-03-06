## Overview

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of aiohttp.

## Requirements
Python 3.8+

## Usage
To run the server, please execute the following from the root directory:

```
docker run --rm -d -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=urlshortener postgres:10
pip3 install -r requirements.txt
python3 -m api_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your OpenAPI definition lives here:

```
http://localhost:8080/openapi.json
```

## Running with Docker

To run the server on a Docker container, please execute the following from the aiohttp directory:

```bash
# building the image
docker build -t api_server .

# starting up a container
docker run -p 8080:8080 api_server
```
