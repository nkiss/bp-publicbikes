# Stage 1: Install dependencies
FROM python:3.12 AS builder

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.12

ENV RUN_INTERVAL=1800

WORKDIR /usr/src/app
COPY --from=builder /install /usr/local
COPY . .
RUN chmod +x /usr/src/app/entrypoint.sh

CMD ["./entrypoint.sh"]