import json
import socket
import argparse
import logging
from client.client_handlers import parse_message
import client.client_statuses as status
from common.colorcon import colors

logger = logging.getLogger('client')
text_attr = colors()

parser = argparse.ArgumentParser()
parser.add_argument('port', type=int, default=7777, help='server port')
parser.add_argument('addr', type=str, default='localhost', help='server address')
parser.add_argument('-m', '--mode', default='listen', nargs='?')
parser.add_argument('-n', '--name', default='Guest', nargs='?')
arg = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((arg.addr, arg.port))

except ConnectionRefusedError:
    logger.info(f'Невозможно подсоединиться к серверу {arg.addr}:{arg.port}')
    exit()

msg_txt = status.client_presence(arg.name)
msg = json.dumps(msg_txt, ensure_ascii=False)
try:
    s.send(msg.encode('ascii'))
except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
    logger.info(f'Соединение с сервером {arg.addr} было потеряно.')
    print(f'{text_attr.C_BLUE}Соединение с сервером {arg.addr} было потеряно.{text_attr.RESET}')
    exit()

if arg.mode == 'listen':
    print(f'{text_attr.C_BLUE}Режим работы - приём сообщений.{text_attr.RESET}')
else:
    print(f'{text_attr.C_BLUE}Режим работы - отправка сообщений.{text_attr.RESET}')

while True:
    if arg.mode == 'listen':
        try:
            data = s.recv(1024)
            parse_message(data, s)
        except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
            logger.info(f'Соединение с сервером {arg.addr} было потеряно.')
            print(f'{text_attr.C_BLUE}Соединение с сервером {arg.addr} было потеряно.{text_attr.RESET}')
            exit()
    if arg.mode == 'send':
        text = input('Введите сообщение:')
        msg_txt = status.client_message(arg.name, text)
        msg = json.dumps(msg_txt, ensure_ascii=False)
        try:
            s.send(msg.encode('ascii'))
        except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
            logger.info(f'Соединение с сервером {arg.addr} было потеряно.')
            print(f'{text_attr.C_BLUE}Соединение с сервером {arg.addr} было потеряно.{text_attr.RESET}')
            exit()
