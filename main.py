import fastapi_vite_dara
from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="assets/templates")
templates.env.globals["vite_hmr_client"] = fastapi_vite_dara.vite_hmr_client
templates.env.globals["vite_asset"] = fastapi_vite_dara.vite_asset


async def homepage(request):
    return templates.TemplateResponse("index.html", {"request": request})


routes = [
    Route("/", endpoint=homepage),
    Mount(
        fastapi_vite_dara.settings.STATIC_URL,
        StaticFiles(directory=fastapi_vite_dara.settings.STATIC_PATH),
        name="static",
    ),
]

app = Starlette(debug=True, routes=routes)
