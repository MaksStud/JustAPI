from routs.routs import Routs


async def app(scope, receive, send):
    if scope['type'] == 'http':
        path = scope['path']

        response = await Routs().get_resonse(path)
        await response(send)
