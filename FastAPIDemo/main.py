from enum import Enum
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates as jt

app = FastAPI()

x = [1,2]
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = jt(directory="templates")

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Cat:
    def __init__(self, name: str, age: int, colors: list[str]):
        self.name = name
        """Name of the cat."""
        
        self.age = age
        """Age in years."""

        self.colors = colors
        """List of colors the cat has."""

class Color(Enum):
    Black = 1
    White = 2
    Gray = 3
  
p = Color.Black

dogs = [Cat("Mittens", 10, ["black", "white"]), Cat("Max", 8, ["gray"]), Cat("Watson", 1, ["black", "white"]), Cat("Sherlock", 1, ["gray", "white"])]

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    # rendered = templates.TemplateResponse("subdir/item2.html", {"request": request, "id": id, "cats": cats}).body 
    return templates.TemplateResponse("subdir/item.html", 
                                      {
                                          "request": request, 
                                          "id": id, 
                                          "cats": dogs, 
                                          "otherCat": Cat("Other", 4, ["red"]),
                                          "dogOpinion2": "annoying!" 
                                      }
                                     )
