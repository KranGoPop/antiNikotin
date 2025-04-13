from aiohttp import web
import logging

logger = logging.getLogger(__name__)

async def stop_read(request):
    readers = request.app['readers']
    data = await request.json()
    port = data.get("port")
    if not port:
        return web.Response(text="Missing port", status=400)

    transport = readers.pop(port, None)
    if transport:
        transport.close()
        logger.info(f"Stopped reading {port}")
        return web.Response(text="OK")
    else:
        return web.Response(text="Not reading", status=404)
