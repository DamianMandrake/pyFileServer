import _thread
import socket
import sys
sys.path.append("..")
import utils.utilities
import os

class ClientSocket:
    DIR = "/home/rohan/Documents/"
    def __init__(self, ip=None,port=None):
        if ip is None or port is None:
            raise Exception
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port

    # this function must be called on a thread... pass in -1 for list only
    def request_list_and_file(self, index):
        self.socket.connect((self.ip, self.port))
        lenOfList = utils.utilities.ByteHandler.bytesToInt(self.socket.recv(4))
        print(lenOfList)
        liststr = self.socket.recv(lenOfList)
        liststr = liststr.decode('utf8')
        complete = liststr.split(',')
        self.files_list = complete

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
            new_file=None
            try:
                path_to_file = ClientSocket.DIR+string
                mode = "w"
                if not os.path.exists(path_to_file):
                    mode ="w+"

                new_file= open(path_to_file, mode+"b")
                new_file.write(filebytes)
                print("DONE WRITING")
            except Exception as e:
                print(e)
            finally:
                if new_file is not None:
                    new_file.close()
        self.socket.close()


c = ClientSocket('127.0.0.1', 4441)
c.request_list_and_file(0)
