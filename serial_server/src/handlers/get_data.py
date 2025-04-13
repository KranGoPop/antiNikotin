from aiohttp import web

async def get_data(request):
    messages = request.app['messages']
    data = await request.json()
    port = data.get("port")
    if not port:
        return web.Response(text="Missing port", status=400)

    lines = messages.get(port, [])
    messages[port] = []
    return web.json_response(lines)
