# Программа клиента, запрашивающего текущее время
import socket
import json
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('port', type=int, help='server port')
parser.add_argument('addr', type=str, help='server address')
arg = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((arg.addr, arg.port))
s.send(b'sdfsd')
tm = s.recv(1024)
s.close()
print(tm.decode('ascii'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((arg.addr, arg.port))
s.send(json.dumps({"action": "pres", "time": time.time(), "user": {"account_name": "Sergey"}}).encode('ascii'))
tm = s.recv(1024)
s.close()
print(tm.decode('ascii'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((arg.addr, arg.port))
s.send(json.dumps({"action": "presence", "time": time.time(), "u": {"account_name": "Sergey"}}).encode('ascii'))
tm = s.recv(1024)
s.close()
print(tm.decode('ascii'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((arg.addr, arg.port))
s.send(json.dumps({"action": "presence", "time": time.time(), "user": {"account_name": "Sergey"}}).encode('ascii'))
tm = s.recv(1024)
s.close()
print(tm.decode('ascii'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((arg.addr, arg.port))
s.send(json.dumps({"action": "quit", "time": time.time(), "user": {"account_name": "Sergey"}}).encode('ascii'))
tm = s.recv(1024)
s.close()
print(tm.decode('ascii'))
