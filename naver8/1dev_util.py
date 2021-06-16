
import socket
import os 
from _thread import *
import base64
#ctrl + spacebar
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad


key = '!!12345678900987654321!!12345678'
iv = '1234567890123456'
decipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
print("decipher :",decipher)
cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 12345
thread_count =0


server_socket.bind((host, port))


server_socket.listen(5)




print("waiting....")

client_socket, address = server_socket.accept()
print("connect :", address)    

start_new_thread(thread_client, (client_socket,))

thread_count += 1
print('Thread Number : ', thread_count)