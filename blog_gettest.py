"""
Routers are used to share the prefix between diffrent files
share opreations between multiple files
share tags

main file syntax

from fastApi import APIRouter
router= APIRouter(prefix='/blog',tags=['blog'])
@router.get('/)

File calling the router from main file
from APIRouter import blog
app=FastAPI()
app.include_router(blog.router)

"""

from  fastapi import FastAPI
from  fastapi import APIRouter,status,Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
#tags and blog will be removed as they are already defined
    
)
#@app.get('/blogs/{id}',status_code=status.HTTP_200_OK,tags=['TAG']) we will remove the blog as it is defined in prefix


@router.get('/{id}',status_code=status.HTTP_200_OK) # app will be replaced with router

def check(id:int, response:Response):
    if id>5 :
        response.status_code=status.HTTP_404_NOT_FOUND
        return{'error' : f'The {id} is less than5'}
    else:
        response.status_code=status.HTTP_200_OK
        return{'message' : f'The {id} is greater than 5'}