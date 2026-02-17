from routs.routs import Routs
from settings import apps
import importlib


for app_name in apps:
    importlib.import_module(f"{app_name}.routs")


async def app(scope, receive, send):
    if scope['type'] == 'http':
        path = scope['path']

        response = await Routs().get_response(path)
        await response(send)
