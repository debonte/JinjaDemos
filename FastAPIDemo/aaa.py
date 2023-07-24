from fastapi import Request
from fastapi.responses import HTMLResponse
from main import app, templates

@app.get("/new", response_class=HTMLResponse)
async def new(request: Request):
    return templates.TemplateResponse("new.html", 
                                      {
                                          "cat": 5
                                      }
                                     )
 