from routs.routs import Routes
from settings import apps
import importlib


for app_name in apps:
    importlib.import_module(f"{app_name}.routs")


async def app(scope, receive, send):
    if scope['type'] == 'http':
        path = scope['path']

        response = await Routes().get_response(path)
        await response(send)
