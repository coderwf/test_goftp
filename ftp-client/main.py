
# -*- coding:utf-8 -*-
from session import PortSession
from common import decimal_to_bc
class Client(PortSession) :
    def __init__(self,host,port):
        PortSession.__init__(self,host,port)

    def receive_msg(self):
        manager = self.receive_with_bytes_manager(4)
        code    = manager.consume_with_decimal(2)
        msg     = manager.consume_all()
        print code , msg

    def send_msg(self,code,param):
        msg_len   = len(param)
        self.send(decimal_to_bc(msg_len,4))
        self.send(decimal_to_bc(code,2))
        self.send(param)

if __name__ == "__main__":
    client  = Client("127.0.0.1",9999)
    client.start_connect()
    client.send_msg(301,"jack")