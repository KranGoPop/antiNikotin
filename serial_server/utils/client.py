import sys
import requests

SERVER_URL = 'http://localhost:5555'  # адрес твоего сервера

def post(path, data):
    try:
        response = requests.post(f'{SERVER_URL}{path}', json=data)
        print(f"[{response.status_code}] {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def handle_command(argv):
    if len(argv) < 2:
        print("Usage:")
        print("  python client.py start <port> <baudrate>")
        print("  python client.py stop <port>")
        print("  python client.py send <port> <message>")
        print("  python client.py get <port>")
        return

    command = argv[1]

    if command == "start" and len(argv) == 4:
        port = argv[2]
        baudrate = int(argv[3])
        post("/start", {"port": port, "baudrate": baudrate})

    elif command == "stop" and len(argv) == 3:
        port = argv[2]
        post("/stop", {"port": port})

    elif command == "send" and len(argv) >= 4:
        port = argv[2]
        message = " ".join(argv[3:])
        post("/send", {"port": port, "message": message})

    elif command == "get" and len(argv) == 3:
        port = argv[2]
        post("/get", {"port": port})

    else:
        print("Invalid usage.")
        print("Usage:")
        print("  python client.py start <port> <baudrate>")
        print("  python client.py stop <port>")
        print("  python client.py send <port> <message>")
        print("  python client.py get <port>")

if __name__ == "__main__":
    handle_command(sys.argv)
