from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def home():
    return "hello world"


@app.get("/about")
def about():
    dataobj = {
        "name": "Ali",
        "age":  28,
        "subject":"python"
    }
    return dataobj