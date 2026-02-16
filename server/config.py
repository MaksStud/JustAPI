from rouds.response import JsonResponse, HTMLResponse


async def app(scope, receive, send):
    if scope['type'] == 'http':
        path = scope['path']

        if path == '/':
            await HTMLResponse("<p><b>MAIN<b/><p/>")(send)
        elif path == '/contact':
            await HTMLResponse("<p><b>contact<b/><p/>")(send)
        elif path == '/j_test':
            await JsonResponse({"page": "JSON TEST"})(send)
        else:
            await HTMLResponse("<p><b>error<b/><p/>")(send)
