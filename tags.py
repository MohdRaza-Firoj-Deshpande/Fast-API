from typing import Optional
from fastapi import FastAPI, Response, status
from enum import Enum

app =FastAPI()
"""
Tags are used to structure the category By Adding a title
"""


@app.get('/blogs/{id}',status_code=status.HTTP_200_OK,tags=['Tag Of Sever Status']) #Tag

def check(id:int, response:Response):
    if id>5 :
        response.status_code=status.HTTP_404_NOT_FOUND
        return{'error' : f'The {id} is less than5'}
    else:
        response.status_code=status.HTTP_200_OK
        return{'message' : f'The {id} is greater than 5'}
