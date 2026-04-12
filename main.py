from fastapi import FastAPI # Import the FastAPI class
from enum import Enum
from fastapi import status


# Create an instance of the FastAPI application
app= FastAPI() #app is used to start the server
# Define a GET route at the root URL '/'
#You can add Doc and Redoc after the URL to look more about the 
@app.get('/hello') # app is the name that we define and same should be used while starting the file(python -m uvicorn hello:app --reload) We are using
#get method (/hello) should be written after the URL
def Greet():
    return{'message':'Hello World'}


@app.get('/hello/all')

def get_page_size(page,pagesize):
    return{'message':f'The page is{page},and size is {pagesize}'}


@app.get('/blog/{id}')
def get_blog(id:int):
    return{'message':f'Blog with{id}'} # you should add http://127.0.0.1:8000/blog/3

#Path method
class Blogtype(str, Enum): #For Predefined path we use enum parameter
    short = 'short'
    story ='story'
    howto ='howto'

@app.get('/blog/type/{type}')
def blog_type(type: Blogtype):
    return(f'This is the type of blog{type}')


"""
The status code is used to check the status of the application which can be helpfull in getting the error message
such as 404

"""

@app.get('blog/{id}',status_code=satus.)
