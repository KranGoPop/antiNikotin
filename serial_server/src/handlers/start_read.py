from aiohttp import web
import logging
import serial_asyncio
import serial
import asyncio
from src.SerialProtocol import SerialProtocol

logger = logging.getLogger(__name__)

async def start_read(request):
    readers = request.app['readers']
    data = await request.json()
    port = data.get("port")
    baud = data.get("baud", 9600)
    
    if not port:
        return web.Response(text="Missing port", status=400)
    
    if port in readers:
        return web.Response(text="Already reading", status=400)

    try:
        loop = asyncio.get_event_loop()
        transport, protocol = await serial_asyncio.create_serial_connection(
            loop, lambda: SerialProtocol(port, request.app), port, baudrate=baud
        )
        request.app["readers"][port] = transport
        logger.info(f"Started reading {port}")
        return web.Response(text="OK")

    except serial.SerialException as e:
        logger.error(f"Serial error on {port}: {e}")
        return web.Response(text=f"Serial error: {e}", status=404)

    except Exception as e:
        logger.exception("Unexpected error on start")
        return web.Response(text=f"Unexpected error: {e}", status=500)
