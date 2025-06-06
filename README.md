# Globant exercise

Globant exercise consuming URL shortener API by is.gd.

## Requirements

- Docker >= 28.1.1

## Build

```shell
docker build -t test .
docker run --rm -it test
```

## Input

The URLs to shorten are read from the [urls.txt](urls.txt) file. A file with no empty lines. The URLs will be parsed by urllib3's parser which is RFC 3986 and RFC 6874 compliant.
