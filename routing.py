from fastapi import FastAPI, Request
from router.routes import route

app = FastAPI()

#api routing
app.include_router(route)