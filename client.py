from ipaddress import ip_address
from msilib.schema import ListBox
from multiprocessing.connection import Client
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from server import IP_ADDRESS
IP_ADDRESS='127.0.0.1'
PORT=8080
SERVER=None

name=None
listbox=None
text_area=None
text_message=None
label_chat=None
connectbutton=None
refreshbutton=None
disconnectbutton=None


def openChatWindow():
    window=Tk()
    window.title('*_*ip messenger*_*')
    window.geometry('500x500')

    labelname = Label(window,text='Enter Your Name')
    labelname.place(x=20,y=10)

    name = Entry(window,width=30)
    name.place(x=50,y=10)
    name.focus()
    

   # screen_width = openChatWindow.winfo_screenheight()
   # screen_height = openChatWindow.winfo_screenheight()



    connectbutton =  Button(window,text="connect", fg='black', font=("Chalkboard SE", 15), bg="yellow")
    connectbutton.place(x = 250 + 120, y= 100)
    refreshbutton =  Button(window,text="refresh", fg='black', font=("Chalkboard SE", 15), bg="blue")
    refreshbutton.place(x = 250, y= 100 )
    disconnectbutton =  Button(window,text="disconnect", fg='black', font=("Chalkboard SE", 15), bg="red")
    disconnectbutton.place(x = 250 - 150, y= 100)


    window.mainloop()

def setup():
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    openChatWindow()
setup()   