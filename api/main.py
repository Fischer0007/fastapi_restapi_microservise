
from db_app import models
from db_app.db import engine, SessionLocal
# from datetime import datetime
from db_app import schemas

from fastapi import FastAPI
from starlette import status
from starlette.responses import Response
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles


app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")


models.Base.metadata.create_all(engine)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/saving_statistics/", status_code=201)
async def saving_statistics(item: schemas.StatisticsBase):
    db = SessionLocal()
    new_entry = models.Statistics(date=item.date, views=item.views, clicks=item.clicks, cost=item.cost)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return Response(status_code=status.HTTP_201_CREATED), {"date": item.date, "views":item.views,
                                                           "clicks": item.clicks, "cost": item.cost
                                                           }


@app.get("/show_statistics/")
def show_statistics(f_rom, to):
    pass


@app.get("/reset_statistics/")
def reset_statistics():
    pass


@app.get("/delete_statistics/")
def reset_statistics():
    pass