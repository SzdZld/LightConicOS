from JMOT import connect
from JMOT import control


class test:
    def fountion_name(variables, socket):
        #if not have response
        ack = connect.send_message(f"false<<500<<{variables}", socket)
        control.verify(ack)

        #if have response
        ack = connect.send_message(f"false<<501<<{variables}", socket)
        return ack[0]