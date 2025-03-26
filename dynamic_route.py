from fastapi import FastAPI

app = FastAPI()

# simple route
@app.get("/")
def home():
    return "this is our home page"

#dynamic
@app.get("/blog/{user_name}")
def blogpage(user_name):
    return {"page": "blog page", "user_name": user_name}