import socket, json, sys, JMOT, logging

def _verify(response):
        '''
        verify the response from server
        '''
        if response[0]:
            pass
        else:
            print("send error")

with open(r"JMOT\connect.json", 'r') as f:
    connect_info = json.load(f)
    SERVER_IP = connect_info["SERVER_IP"]
    SERVER_DATA_PORT = connect_info["SERVER_DATA_PORT"]
    SERVER_STREAM_PORT = connect_info["SERVER_LIST_PORT"]
    SERVER_BUFFER = connect_info["SERVER_BUFFER"]
    f.close()

logging.basicConfig(filename=r'JMOT\log\tran.log', level=logging.INFO, format='%(asctime)s %(message)s')

def _send_message_with_length(sock, message):
    message_bytes = message.encode('utf-8')
    sock.sendall(message_bytes)

def _receive_message_with_length(sock):
    message_bytes = sock.recv(SERVER_BUFFER)
    if not message_bytes:
        return None
    return message_bytes.decode('utf-8')


def _convert_value(item):
    '''
    Convert the string item to the appropriate type (boolean, 3D vector, float, or string)
    '''
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

def _parse_message_to_list(message):
    ''' Split the message by "<<" delimiter, trim and convert the type of each item'''
    items = message.split("<<")
    return [_convert_value(item) for item in items if item.strip()]

def data_connect():
    '''
    JMOT data connect from Juno New Origin
    '''
    try:
        print("JMOT connecting...")
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, SERVER_DATA_PORT))
        version = _send_message("version", client_socket)[0]
        if version != JMOT.__version__:
            print("version error, please updates")
            sys.exit(1)
        else:
            print(f"JMOT v{JMOT.__version__} connect successful")
        return client_socket
    except Exception as e:
        print(f"Error occurred: {e}")

def _send_message(message:str, socket = None):
    '''
    send message to server and receive response
    '''
    if socket is None:
        socket = client_socket
    try:
        _send_message_with_length(socket, message)
        logging.info(f'<- {message}')
        response = _receive_message_with_length(socket)
        if response is None or not _convert_value(response):
            logging.info("Send Failed")
            print("Send Failed")
        else:
            data = _parse_message_to_list(response)
            logging.info(f'-> {data}')
            return data

    except Exception as e:
        print(f"Error occurred: {e}")