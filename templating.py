from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pymongo

app = FastAPI()

#conecting with mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["friends"]
collection = database["best_friend"]

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/{name}", response_class=HTMLResponse)
def read_item(request: Request, name):
    collection.insert_one({"name": name})
    return templates.TemplateResponse(
        request=request, name="home.html",
    )


@app.get("/about", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="about.html",
    )