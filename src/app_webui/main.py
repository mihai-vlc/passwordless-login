from app_webui.config import APP_SESSION_KEY, STATIC_FOLDER, TEMPLATES_FOLDER
from passwordless import LOGIN_TYPE
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse

from starsessions import CookieStore, SessionAutoloadMiddleware, SessionMiddleware, regenerate_session_id


app = FastAPI()

app.add_middleware(SessionAutoloadMiddleware)
app.add_middleware(SessionMiddleware, store=CookieStore(
    secret_key=APP_SESSION_KEY))

app.mount("/static", StaticFiles(directory=STATIC_FOLDER), name="static")

templates = Jinja2Templates(directory=TEMPLATES_FOLDER)


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    context = {
        "request": request,
        "login_type": LOGIN_TYPE,
        "username": request.session.get("username", "Anonymous")
    }
    return templates.TemplateResponse("index.html", context)


@app.get("/login", response_class=RedirectResponse)
async def login(request: Request):
    regenerate_session_id(request)
    request.session["username"] = "mihai"
    return "/"


@app.get("/logout", response_class=RedirectResponse)
async def logout(request: Request):
    request.session.clear()
    return "/"


def run():
    return 0


if __name__ == "__main__":
    exit(run())
