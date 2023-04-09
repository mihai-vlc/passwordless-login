
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

BASE_PATH = Path(__file__).parent
STATIC_FOLDER = BASE_PATH.joinpath("static")
TEMPLATES_FOLDER = BASE_PATH.joinpath("templates")

print(STATIC_FOLDER)
app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_FOLDER), name="static")

templates = Jinja2Templates(directory=TEMPLATES_FOLDER)


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("index.html", context)


def run():
    return 0


if __name__ == "__main__":
    exit(run())
