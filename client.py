import socket
import datetime
import select

# connect_to_host, check_timeout, diconnect, send_data, reciv_data, save_data_to_file

class Client():

    def __init__(self, client_ip="127.0.0.1", client_port=4567): # <-- to jest raczej adres servera, do ktorego sie laczy klient
        print("[*]Nawiazuje polaczenie", client_ip, client_port) # <-- chcialbym wiedziec z czym sie lacze :)
        # -------------------------
        self.__local_ip = client_ip
        self.__local_port = client_port
        # -------------------------
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_remote_socket(self):

        self.client.connect((self.__local_ip, self.__local_port))

    def send_data(self):
        """"""
        data = input("(Me)>>>")
        self.client.send(data.encode('utf-8'))

    def recv_data(self):
        """"""
        # Receive and return
        inputs = []
        outputs = []


        recived_data = self.client.recv(1024)
        return recived_data

    def close_connection(self):
        """"""
        # self.client.shutdown()
        self.client.send(b"")
        self.client.close()

client = Client()
client.connect_to_remote_socket() # <-- brakowalo tego

dataFrom_RemoteSocket = client.recv_data()
print('RECV:', dataFrom_RemoteSocket.decode("utf-8")) # <-- nawias w złym miejscu

while True:
    print("[*]Connect to remote socket")
    print("[*]send data")
    client.send_data()
    #Show response
