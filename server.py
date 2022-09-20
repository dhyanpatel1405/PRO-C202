from ipaddress import ip_address
from multiprocessing.connection import Client
import socket
from threading import Thread
IP_ADDRESS='127.0.0.1'
PORT=8080
SERVER=None
CLIENT={}


def addclients():
    global SERVER
    global CLIENT

    while True:
        client, addr = SERVER.accept()
        print(client, addr)


def setup():
    print('\n\n\n\n\n\t\t\t\t\t\t***IP MESSENGER***')


    global PORT
    global IP_ADDRESS
    global SERVER


    SERVER  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    addclients()


setup_thread = Thread(target=setup)           
setup_thread.start()