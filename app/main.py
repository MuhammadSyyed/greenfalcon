from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Home page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# PDF content page
@app.get("/catalog")
def pdf_content(request: Request):
    return templates.TemplateResponse("pdfContent.html", {"request": request})

# Serve catalog.json
@app.get("/catalog.json")
def get_catalog():
    return FileResponse("app/static/catalog.json")

# Serve catalog.pdf
@app.get("/catalog.pdf")
def get_pdf():
    return FileResponse("app/static/catalog.pdf")
