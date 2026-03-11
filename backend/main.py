import asyncio

from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def salute(name: str):
    return {"message": f"Hello {name}"}

@app.get("/hello-async")
async def hello_async():
    await asyncio.sleep(1)
    return {"message": "Hello async"}
