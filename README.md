 <h1 align="center">Fastapi - REST API Microservise</h1>
 
 ## Requirements

- [Docker >= 17.05] ...
- [Python >= 3.10](https://www.python.org/downloads/release/python-3100/)
- [Poetry](https://github.com/python-poetry/poetry)
 
 ## Local development

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
