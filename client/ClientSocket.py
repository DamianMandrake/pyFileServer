import _thread
import socket
import sys
sys.path.append("..")
import utils.utilities
import os
from os.path import expanduser


class ClientSocket:
    DIR = expanduser("~")+"/Downloads/"

    def __init__(self, ip=None,port=None):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    def set_port_and_ip(self, port, ip):
        self.port = port
        self.ip = ip

    # this function must be called on a thread... pass in -1 for list only
    def request_list_and_file(self, index, list_callback, success_callback):
        self.socket.connect((self.ip, self.port))
        lenOfList = utils.utilities.ByteHandler.bytesToInt(self.socket.recv(4))
        print(lenOfList)
        liststr = self.socket.recv(lenOfList)
        liststr = liststr.decode('utf8')
        complete = liststr.split(',')

        list_callback(complete)
        self.socket.send(utils.utilities.ByteHandler.intToBytes(index))

        if index != -1:
            # receiving length of file
            length = utils.utilities.ByteHandler.bytesToInt(self.socket.recv(4))
            filebytes = self.socket.recv(length)
            print(filebytes)
            string = str(self.files_list[index])
            string = string.replace('[', '')
            string = string.replace("\'", '')
            string = string.replace("]", '')
            print(string)
            new_file = None
            try:
                path_to_file = ClientSocket.DIR+string
                mode = "w"
                if not os.path.exists(path_to_file):
                    mode ="w+"

                new_file= open(path_to_file, mode+"b")
                new_file.write(filebytes)
                print("DONE WRITING")
                success_callback(True)
            except Exception as e:
                print(e)
                success_callback(False)
            finally:
                if new_file is not None:
                    new_file.close()

        self.socket.close()

#
# def list_callback(list):
#     print(list)
#
#
# def file_success_callback(file):
#     print(file)

#
# c = ClientSocket('192.168.1.103', 4444)
# c.request_list_and_file(0,list_callback,file_success_callback)
