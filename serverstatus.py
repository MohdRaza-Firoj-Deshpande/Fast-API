from typing import Optional
from fastapi import FastAPI, Response, status
from enum import Enum

app =FastAPI()



@app.get('/blogs/{id}',status_code=status.HTTP_200_OK)

def check(id:int, response:Response):
    if id>5 :
        response.status_code=status.HTTP_404_NOT_FOUND
        return{'error' : f'The {id} is less than5'}
    else:
        response.status_code=status.HTTP_200_OK
        return{'message' : f'The {id} is greater than 5'}
