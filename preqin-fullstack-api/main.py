from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import investor_controller

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(CORSMiddleware, allow_origins=origins)


# Future considerations for an ORM are Tortoise ORM (async by default) or PeeWee (fast, powerful)
# https://www.infoworld.com/article/2335270/6-orms-for-every-database-powered-python-app.html
@app.get("/")
async def root():
    return {"message": "Hello World"}
