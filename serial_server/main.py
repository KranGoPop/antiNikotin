import asyncio
import logging
import serial_asyncio
from aiohttp import web
from src.handlers import send_to_serial, get_data, start_read, stop_read

# --- ЛОГГЕР ---
logger = logging.getLogger("serial_server")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("server.log")
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

app = web.Application()
app.add_routes([
    web.post("/start", start_read),
    web.post("/stop", stop_read),
    web.post("/get", get_data),
    web.post("/send", send_to_serial),
])

app['readers'] = {}
app['messages'] = {}

if __name__ == "__main__":
    web.run_app(app, port=5555)

