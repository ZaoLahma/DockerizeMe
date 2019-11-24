import socket

class NwMisc:
    ADDRESS = None
    @staticmethod
    def get_own_address():
        if None == ADDRESS:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('5.255.255.255', 1))
            ADDRESS = s.getsockname()[0]
            s.close()
        return ADDRESS