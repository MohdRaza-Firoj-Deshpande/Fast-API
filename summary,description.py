from typing import Optional
from fastapi import FastAPI, Response, status
from enum import Enum

app =FastAPI()
"""
Summary is small peice of text 
While Desciption is a more defined context
"""


@app.get('/blogs/{id}',status_code=status.HTTP_200_OK,tags=['Tag Of Sever Status'],summary='This is Server Code Check')

def check(id:int, response:Response):
    """This is the summary
    - **id** mandotry path parameter
    """
    if id>5 :
        response.status_code=status.HTTP_404_NOT_FOUND
        return{'error' : f'The {id} is less than5'}
    else:
        response.status_code=status.HTTP_200_OK
        return{'message' : f'The {id} is greater than 5'}
    

    
