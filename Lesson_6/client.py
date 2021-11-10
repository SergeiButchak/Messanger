# Программа клиента, запрашивающего текущее время
import socket
import json
import time
import argparse
import logging
import log.client_log_config

logger = logging.getLogger('client')

parser = argparse.ArgumentParser()
parser.add_argument('port', type=int, help='server port')
parser.add_argument('addr', type=str, help='server address')
arg = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((arg.addr, arg.port))
except ConnectionRefusedError:
    logger.info(f'Невозможно подсоединиться к серверу {arg.addr}:{arg.port}')
    exit()
s.send(b'sdfsd')
tm = s.recv(1024)
s.close()
logger.debug(f'Получено сообщение от сервера: {tm.decode("ascii")}')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((arg.addr, arg.port))
except ConnectionRefusedError:
    logger.info(f'Невозможно подсоединиться к серверу {arg.addr}:{arg.port}')
    exit()
s.send(json.dumps({"action": "pres", "time": time.time(), "user": {"account_name": "Sergey"}}).encode('ascii'))
tm = s.recv(1024)
s.close()
logger.debug(f'Получено сообщение от сервера: {tm.decode("ascii")}')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((arg.addr, arg.port))
except ConnectionRefusedError:
    logger.info(f'Невозможно подсоединиться к серверу {arg.addr}:{arg.port}')
    exit()
s.send(json.dumps({"action": "presence", "time": time.time(), "u": {"account_name": "Sergey"}}).encode('ascii'))
tm = s.recv(1024)
s.close()
logger.debug(f'Получено сообщение от сервера: {tm.decode("ascii")}')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((arg.addr, arg.port))
except ConnectionRefusedError:
    logger.info(f'Невозможно подсоединиться к серверу {arg.addr}:{arg.port}')
    exit()
s.send(json.dumps({"action": "presence", "time": time.time(), "user": {"account_name": "Sergey"}}).encode('ascii'))
tm = s.recv(1024)
s.close()
logger.debug(f'Получено сообщение от сервера: {tm.decode("ascii")}')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((arg.addr, arg.port))
except ConnectionRefusedError:
    logger.info(f'Невозможно подсоединиться к серверу {arg.addr}:{arg.port}')
    exit()
s.send(json.dumps({"action": "quit", "time": time.time(), "user": {"account_name": "Sergey"}}).encode('ascii'))
tm = s.recv(1024)
s.close()
logger.debug(f'Получено сообщение от сервера: {tm.decode("ascii")}')
