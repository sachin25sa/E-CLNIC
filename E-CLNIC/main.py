from ast import For
from datetime import datetime
from turtle import st
from urllib import response
from fastapi import FastAPI, Request, Cookie
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# creating a FastAPI object
app = FastAPI()

#configuring the static, which serve static
app.mount("/static", StaticFiles(directory="static"), name="static")

#configuring the HTML pages
templates = Jinja2Templates(directory="templates")

#declaring urls
@app.get("/", response_class=HTMLResponse)
def bootstrap(request : Request):
    return templates.TemplateResponse("bootstrap.html", { "request" : request })



