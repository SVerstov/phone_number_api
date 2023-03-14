from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from searcher import search_number_info
from tasks import start_periodic_task

start_periodic_task()

app = FastAPI()
# Add the CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/api/')
def number_info(number: str):
    return search_number_info(number)


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)
