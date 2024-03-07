from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datamodel.datamodel import TestDataModel, DataModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_data_model() -> DataModel:
    return TestDataModel()


@app.get("/")  # type: ignore
async def root(request: Request) -> HTMLResponse:
    dm = get_data_model()
    fighters = dm.get_fighters()
    return templates.TemplateResponse(
        request=request, name="index.html", context={"fighters": fighters}
    )
