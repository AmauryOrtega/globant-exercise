FROM python:3.13-alpine

RUN apk add --no-cache uv

WORKDIR /app
COPY . .
RUN uv sync

CMD ["uv", "run", "main.py"]
