from tkinter import *
import sys
sys.path.append("client/ClientSocket")
import ClientSocket

cs = ClientSocket.ClientSocket()
root = Tk()
ip_text = Text(root, height=2, width = 80)#ip
port_text = Text(root,height=2,width = 30)#port
ip_text.pack()
port_text.pack()
files_list = []


def set_files_list(list):
    files_list = list
    i =0
    for string in files_list:
        string = string.replace('[', '')
        string = string.replace("\'", '')
        string = string.replace("]", '')
        listbox.insert(i, string)
        i = i+1


def file_callback(status):
    print(status)


def list_item_selected(evt):
    print(listbox.get(ACTIVE))


def action():
    port = int(port_text.get("1.0",END).replace('\n',''))
    ip = ip_text.get("1.0",END).replace('\n','')
    cs.set_port_and_ip(port, ip)
    cs.request_list_and_file(-1,set_files_list,)


button = Button(root, text="Connect", command=action)
button.pack()
listbox = Listbox(root)
listbox.pack()
root.mainloop()