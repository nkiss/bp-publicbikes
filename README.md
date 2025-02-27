
# Budapest Public Bikes
This project is about the play with the public data of Budapest public bikes.

## Create the Azure environment
### What is needed
1. Storage account
2. Databricks
3. Container apps

### How it works
1. Collecting the data from public REST APIs
2. Save the result into the Data Lake (Storage account)
3. Clean and Transform the code with Databricks
4. Play with the data

## Build
### Container

```bash
# Build with the version 0.1
docker build -f Containerfile -t bp-publicbikes:0.1 .

# Run every minute
docker run -it --rm -e RUN_INTERVAL=60 bp-publicbikes:0.1 bash
```

```bash

```


```py

```

```bash
$ python -m bp_publicbikes
#or
$ bp_publicbikes
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
