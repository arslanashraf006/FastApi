from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pymongo

app = FastAPI()

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["person"]
collection = database["employee"]


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_item(request: Request,):

    return templates.TemplateResponse(
        request=request, name="home.html",
    )


@app.get("/about", response_class=HTMLResponse)
def read_item(request: Request):
    # name = "Ali"
    # age = 15
    # subject = "web development"

    # user = {
    #     "name": name,
    #     "age": age,
    #     "subject": subject,
    # }
    user = []
    raw_data = collection.find()
    for item in raw_data:
        print(item)
        user.append(item)
    print(user)
    return templates.TemplateResponse(
        request=request, name="about.html", context= {"user":user }
    )
    # return templates.TemplateResponse(
    #     request=request, name="about.html", context= {"fruits": ["apple", "mango", "guave", "pineapple", "banana", "grapes"]}
    # )





# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/hello")
# def home():
#     return "hello world"


# @app.get("/about")
# def about():
#     dataobj = {
#         "name": "Ali",
#         "age":  28,
#         "subject":"python"
#     }
#     return dataobj