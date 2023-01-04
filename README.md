 <h1 align="center">Fastapi - REST API Microservise</h1>
 
 ## Requirements

- [Docker >=  20.10.20](https://docs.docker.com/engine/install/ubuntu/)
- [PostgreSQL >= 14](https://www.postgresql.org/download/linux/ubuntu/)
- [Python >= 3.10](https://www.python.org/downloads/release/python-3100/)
- [Poetry](https://github.com/python-poetry/poetry) 
 
 ## Local development

### PostgreSQL


Create the file repository configuration:

```shell
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

Import the repository signing key:

```shell
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

Update the package lists:

```shell
sudo apt-get update
```

Install the latest version of PostgreSQL.
If you want a specific version, use 'postgresql-14' or similar instead of 'postgresql':

```shell
sudo apt-get -y install postgresql-14
```

### Poetry


Create the virtual environment and install dependencies with:

```shell
poetry install
```

See the [poetry docs](https://python-poetry.org/docs/) for information on how to add/update dependencies.

Run commands inside the virtual environment with:

```shell
poetry run <your_command>
```

Spawn a shell inside the virtual environment with:

```shell
poetry shell
```

Start a development server locally:

```shell
poetry run uvicorn api.main:app --reload --host localhost --port 8000
```

API will be available at [localhost:8000/](http://localhost:8000/)

- Swagger UI docs at [localhost:8000/docs](http://localhost:8000/docs)
- ReDoc docs at [localhost:8000/redoc](http://localhost:8000/redoc)
