import socket;
import _thread;
import os;
import sys
sys.path.append("..")
import utils.utilities

''' This class can as of now only share 1 folder. It listens for connections on PORT 444'''


class Server:
    PORT = 4444
    MAX_ACTIVE_CONNECTIONS = 20
    HOST = socket.getfqdn()

    def __init__(self, port=None, foldername="~/Documents"):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.file_handler = Server.FileHandler(foldername)

        # using default port
        if port is None or port < 0 or port > 65535:
            self.socket.bind((Server.HOST, Server.PORT))
        else:
            self.socket.bind((Server.HOST, port))

        self.socket.listen(Server.MAX_ACTIVE_CONNECTIONS)

    def start_server(self):
        while True:
            try:
                stream, address = self.socket.accept()
                _thread.start_new_thread(self.handle_user, (stream,"thread"))
            except Exception as e:
                print(e)
                stream.close()


    def handle_user(self, stream, threadname):
        string = str(self.file_handler.get_list_of_files())
        b = utils.utilities.ByteHandler.intToBytes(len(string))
        print("LEN", b[0])

        stream.send(b)
        print(string)

        stream.send(string.encode('utf8'))
        data = utils.utilities.ByteHandler.bytesToInt(stream.recv(4))
        print("requested index ", data)
        if data != 4294967295:
            print( self.file_handler.get_list_of_files()[data])
            filebytes = self.file_handler.get_file_bytes(index=data)
            # sending length of the file
            print("len of file ",len(filebytes))
            stream.send(utils.utilities.ByteHandler.intToBytes(len(filebytes)))
            # sending file
            for b in filebytes:
                stream.send(b)

        print("about to leave thread")
        stream.close()

    def close(self):
        self.socket.close();

    class FileHandler:
        def __init__(self, folder):
            self.folder = folder
            self.list_of_files = os.listdir(folder)

        # this function returns a list of files in the directory
        def get_list_of_files(self):
            return self.list_of_files

        # this function returns the contents of a file in bytes given its index from the list
        def get_file_bytes(self, index):
            print(self.folder+"/"+self.list_of_files[index])
            currentfile = open(self.folder+"/"+self.list_of_files[index], "r+b")
            data = []
            try:
                byte = currentfile.read(1)
                while byte:
                    data.append(byte)
                    byte = currentfile.read(1)
            except Exception as e:
                print(e)
            finally:
                currentfile.close()
            print(data)
            return data


c = None
try:
    c = Server(foldername="/home/rohan/Documents/c_workspace/temp", port=4441)
    c.start_server()
except Exception as e:
    if c is not None:
        c.close()
    print(e)