from cryptography.fernet import Fernet
from tkinter import *
import socket
from tkinter import messagebox
import os
import time

# sending text  ..................................................................................

def send_text():
    f = Fernet(key)
    token = f.encrypt(str.encode(post_cmd.get()))
    print(token)
    s.send(token)
    # s.send(key)

    posts.destroy()

# sending file --------------------------------------------

def send_file():
    global file_name
    global file_path
    print(file_name.get(),file_path.get())
    fd = os.open(file_path.get(),os.O_RDONLY)
    n = os.path.getsize(file_path.get())
    print(n)
    read_bytes = os.read(fd,n)
    print(read_bytes)
    data = "File"+file_name.get()+"^"+str(read_bytes,"utf-8")
    f = Fernet(key)
    token = f.encrypt(str.encode(data))
    s.send(token)
    posts.destroy()

# disconnect ..................................................................................
def disconnects():
    s.send(str.encode("Disconnect"))
    s.close()
    print('Disconnected to server...')
    root.destroy()

# Transfering file ----------

def File_transfer():
    global posts
    global file_name
    global file_path
    posts = Toplevel(root)
    posts.geometry('600x600')
    file_name = StringVar()
    file_path = StringVar()
    Label(posts, text="Enter the File name : ").place(x=40, y=50)
    Entry(posts, textvariable=file_name).place(x=250, y=50)
    Label(posts, text="Enter the File path : ").place(x=40, y=100)
    Entry(posts, textvariable=file_path).place(x=250, y=100)
    Button(posts, text='Send', command=send_file, fg="green").place(x=300, y=150)
    posts.bind('<Return>', lambda event=None: send_file())
    posts.mainloop()


# connects ..................................................................................
def displays_conn():
    connec.destroy()
    print("IP address : ", ip_add.get(), "\nPort Number :", port_num.get())
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ip_add.get()
    port = port_num.get()
    s.connect((host, port))  # here we just connect the server
    messagebox.showinfo('Status', "Connection Established")
    s.send(key)


def connects():
    global connec
    global ip_add
    global port_num
    connec = Toplevel(root)
    connec.geometry('600x600')

    ip_add = StringVar()
    port_num = IntVar()

    Label(connec, text='Enter IP address : ').place(x=40, y=50)
    Entry(connec, textvariable=ip_add).place(x=250, y=50)

    Label(connec, text='Enter Port Number : ').place(x=40, y=150)
    Entry(connec, textvariable=port_num).place(x=250, y=150)

    Button(connec, text='Connect', command=displays_conn).place(x=400, y=100)
    connec.bind('<Return>', lambda event=None: displays_conn())
    connec.mainloop()


# menu ..................................................................................

def adjustWindow(window):
    w = 600  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)  # calculate x and y coordinates for the Tk window
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(False, False)  # disabling the resize option for the window
    # window.configure(background='#174873') # making the background white of the window


# validate the entry data and makes a new entry into the database


def menu():
    global root
    global key
    key = Fernet.generate_key()

    # global s
    root = Tk()
    adjustWindow(root)
    Label(root, text="Encrypted Data Transfer System", width="500", height="2", font=("Calibri", 22, 'bold'), fg='white',
          bg='green').pack()
    Button(root, text='Connect', command=connects, fg="green").place(x=50, y=150)
    Button(root, text='Disconnect', command=disconnects, fg="red").place(x=250, y=150)
    Text_button = Button(root, text='Text Transfer', command=Text_transfer, fg="blue")
    Text_button.place(x=50, y=250)
    Button(root, text='File Transfer', command=File_transfer, fg="blue").place(x=250, y=250)

    root.bind('<Escape>', lambda event=None: root.destroy())
    root.mainloop()

menu()