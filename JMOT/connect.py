import socket, json, sys, JMOT, logging

with open(r"JMOT\log\connect.json", 'r') as f:
    connect_info = json.load(f)
    SERVER_IP = connect_info["SERVER_IP"]
    SERVER_DATA_PORT = connect_info["SERVER_DATA_PORT"]
    SERVER_STREAM_PORT = connect_info["SERVER_STREAM_PORT"]
    SERVER_BUFFER = connect_info["SERVER_BUFFER"]
    f.close()

<<<<<<< HEAD
logging.basicConfig(filename=r'JMOT\log\tran.log', level=logging.INFO, format='%(asctime)s %(message)s')
=======
logging.basicConfig(filename=r'JMOT\tran.log', level=logging.INFO, format='%(asctime)s %(message)s')
>>>>>>> e5ec67a975e4902d31ba3d7cd43c1e69193ceaf3

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

def data_connect():
    try:
        print("JMOT connecting...")
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_DATA_PORT))
        version = send_message("version", client_socket)[0]
        if version != JMOT.__version__:
            print("version error, please updates")
            sys.exit(1)
        else:
            print(f"JMOT v{JMOT.__version__} connect successful")
        return client_socket
    except Exception as e:
        print(f"Error occurred: {e}")

def send_message(message:str, socket = None):
    if socket is None:
        socket = client_socket
    try:
        send_message_with_length(socket, message)
        logging.info(f'-> {message}')
        response = receive_message_with_length(socket)
        if response is None or not convert_value(response):
            logging.info("Send Failed")
            print("Send Failed")
        else:
            data = parse_message_to_list(response)
            logging.info(f'<- {data}')
            return data

    except Exception as e:
        print(f"Error occurred: {e}")
