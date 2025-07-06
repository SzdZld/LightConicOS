from Telemetry import connect

class display():
    def display(message:str, socket):
        connect.send_message(f"false<<display<<{message}", socket)

    def local_log(message:str, socket):
        connect.send_message(f"false<<lolog<<{message}", socket)

    def flight_log(message:str, override:bool, socket):
        connect.send_message(f"false<<fllog<<{message}<<{override}", socket)
