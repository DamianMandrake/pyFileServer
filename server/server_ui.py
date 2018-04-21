from tkinter import *
import sys
sys.path.append("server/Server")

import Server
import _thread

server = Server.Server(None)
text = None


def button_callback():
    print("call")
    string = text.get("1.0", END)
    string = string.replace('\n', '')
    server.set_dir(string)
    _thread.start_new(server.start_server(),())


root = Tk()
root.winfo_toplevel().title("server")
text = Text(root, height=4, width=100)
text.pack()
button = Button(root, text="start server",command=button_callback)
button.pack()

root.mainloop()
