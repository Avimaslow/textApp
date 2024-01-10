import socket
from tkinter import Tk, Scrollbar, Entry, Button, END, Listbox
from tkinter.ttk import Frame, Style

def sendMsg(listbox, entry):
    message = entry.get()
    listbox.insert('end', "Client: " + message)
    entry.delete(0, END)
    s.send(bytes(message, 'utf-8'))
    recieveMsg(listbox)

def recieveMsg(listbox):
    message = s.recv(40)
    listbox.insert('end', "Server: " + message.decode('utf-8'))

# Networking setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
PORT = 12398
s.connect((host_name, PORT))

# GUI setup
root = Tk()
root.title('Client Chat Application')

style = Style()
style.theme_use('clam')  # You can choose other themes like 'alt', 'default', or 'classic'

frame = Frame(root)
frame.pack(padx=10, pady=10)

listbox = Listbox(frame, height=15, width=50)
scroll_bar = Scrollbar(frame, command=listbox.yview)
listbox['yscrollcommand'] = scroll_bar.set

entry = Entry(frame, width=48)
send_button = Button(frame, text="Send", command=lambda: sendMsg(listbox, entry))
recieve_button = Button(frame, text="Recieve", command=lambda: recieveMsg(listbox))

listbox.grid(row=0, column=0, columnspan=2)
scroll_bar.grid(row=0, column=2, sticky='nsew')
entry.grid(row=1, column=0, padx=5, pady=10)
send_button.grid(row=1, column=1, padx=5)
recieve_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
