from aiohttp import web
import logging

logger = logging.getLogger(__name__)

async def send_to_serial(request):
    readers = request.app['readers']
    data = await request.json()
    port = data.get("port")
    message = data.get("message")

    if not port or message is None:
        return web.Response(text="Missing port or message", status=400)

    if port not in readers:
        return web.Response(text="Not reading", status=404)

    try:
        readers[port].write((message + "\n").encode())
        logger.info(f"Sent to {port}: {message}")
        return web.Response(text="SENT")
    except Exception as e:
        logger.exception(f"Error sending to {port}")
        return web.Response(text=f"Error: {e}", status=500)
