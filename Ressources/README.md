# Fincome Project

## Introduction

This project is an API that permit to shortening URL.

## Useful commands

- To build the project

```
docker build -t fincome-url-shortener .
```

- To launch the project

```
docker run -p 5000:5000 fincome-url-shortener
```

## API Endpoints

- Encoding Url

```
POST : http://127.0.0.1:5000/encode
Data:
'{
    "url": "https://www.fincome.co/"
}'
```

- Decoding Url

```
POST : "http://127.0.0.1:5000/decode"
Data:
'{
  "short_url": "http://short.est/xxxxx"
}'
```