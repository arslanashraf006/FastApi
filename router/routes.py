from fastapi import APIRouter, Request

route =  APIRouter()

@route.get("/")
def homepage(request: Request):
    return "this is our home page"


@route.get("/about")
def aboutpage(request: Request):
    return "this is our about page"