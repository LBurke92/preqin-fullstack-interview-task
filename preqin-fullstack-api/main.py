from fastapi import FastAPI

app = FastAPI()

# Future considerations for an ORM are Tortoise ORM (async by default) or PeeWee (fast, powerful)
# https://www.infoworld.com/article/2335270/6-orms-for-every-database-powered-python-app.html
@app.get("/")
async def root():
    return {"message": "Hello World"}