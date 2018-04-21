from tkinter import *
import sys
sys.path.append("server/Server")

import Server

server = Server.Server(None)
text = None


def button_callback():
    print("call")
    string = text.get("1.0", END)
    string = string.replace('\n', '')
    server.set_dir(string)


root = Tk()
root.winfo_toplevel().title("server")
text = Text(root, height=4, width=100)
text.pack()
button = Button(root, text="start server",command=button_callback)
button.pack()

root.mainloop()
