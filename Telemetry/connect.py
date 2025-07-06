import socket
import json
import sys

with open(r"Telemetry\connect.json", 'r') as f:
    connect_info = json.load(f)
    VERSION = connect_info["Version"]
    if VERSION != "0.1.a1":
        print("please update to new version")
        sys.exit()
    SERVER_IP = connect_info["SERVER_IP"]
    SERVER_PORT = connect_info["SERVER_PORT"]
    SERVER_BUFFER = connect_info["SERVER_BUFFER"]


def send_message_with_length(sock, message):
    message_bytes = message.encode('utf-8')
    sock.sendall(message_bytes)

def receive_message_with_length(sock):
    message_bytes = sock.recv(SERVER_BUFFER)
    if not message_bytes:
        return None
    return message_bytes.decode('utf-8')

def convert_value(item):
    s = item.strip()
    # Attempt to convert to boolean
    if s.lower() == "true":
        return True
    if s.lower() == "false":
        return False

    # Attempt to convert to a 3D vector (a, b, c)
    if s.startswith("(") and s.endswith(")"):
        inner = s[1:-1]
        parts = inner.split(',')
        if len(parts) == 3:
            try:
                return (float(parts[0].strip()), float(parts[1].strip()), float(parts[2].strip()))
            except ValueError:
                pass

    # Attempt to convert to a floating point number
    try:
        return float(s)
    except ValueError:
        pass

    # Return the original string if no conversion applies
    return s

def parse_message_to_list(message):
    # Split the message by "<<" delimiter, trim and convert the type of each item
    items = message.split("<<")
    return [convert_value(item) for item in items if item.strip()]

def connect():
    try:
        # Test Connect
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_PORT))
        return client_socket
    except Exception as e:
        print(f"Error occurred: {e}")



def send_message(message:str, skt):
    try:
        send_message_with_length(client_socket, message)
        response = receive_message_with_length(client_socket)
        if response is None or not convert_value(response):
            print("Send Failed")
        else:
            return response


    except Exception as e:
        print(f"Error occurred: {e}")
    # finally:
    #     client_socket.close()
