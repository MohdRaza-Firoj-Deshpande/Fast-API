from fastapi import FastAPI
from router import routers

app = FastAPI()
app.include_router(routers.router)

@app.get('/')
def hello():
    return 'Hello world'

