
import fastapi
from db_app import models
from db_app.db import engine, SessionLocal, Base
from db_app import schemas

from fastapi import FastAPI, requests, Request, Form, Path
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
    return Response(status_code=status.HTTP_201_CREATED), {"date": item.date, "views": item.views,
                                                           "clicks": item.clicks, "cost": item.cost
                                                           }


@app.post(f"/show_statistics/")
async def show_statistics(date_from: str = Form(regex=r'^\d{4}\-\d\d\-\d\d$'),
                          date_to: str = Form(regex=r'^\d{4}\-\d\d\-\d\d$')):
    db = SessionLocal()
    mydate = db.query(models.Statistics).filter(models.Statistics.date >= date_from).\
        filter(models.Statistics.date <= date_to)
    list_response = []
    for i in mydate:
        list.append(i)
    # print(*list_response, sep='\n')
    response = list_response
    return Response(status_code=status.HTTP_200_OK), response


@app.get("/reset_statistics/")
def reset_statistics():
    db = SessionLocal()
    db.query(models.Statistics).delete()
    db.commit()
    return Response(status_code=status.HTTP_200_OK), "Статистика сброшена"


@app.get("/clearn_statistics/")
def clearn_statistics():
    Base.metadata.drop_all(engine)
    return Response(status_code=status.HTTP_200_OK), "Таблица со статистикой удалена"
