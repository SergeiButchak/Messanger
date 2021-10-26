"""
1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
Функции клиента:
    сформировать presence-сообщение;
    отправить сообщение серверу;
    получить ответ сервера;
    разобрать сообщение сервера;
    параметры командной строки скрипта client.py <addr> [<port>]:
    addr — ip-адрес сервера;
    port — tcp-порт на сервере, по умолчанию 7777.
Функции сервера:
    принимает сообщение клиента;
    формирует ответ клиенту;
    отправляет ответ клиенту;
    имеет параметры командной строки:
    -p <port> — TCP-порт для работы (по умолчанию использует 7777);
    -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

Задание:
1.) Изменить имена переменных и функций в предоставленном скрипте (чем больше, тем лучше);
2.) Изменить порядок пары ip_адрес-порт на порт-ip_адрес : <port> [<addr>]:
3.) Добавить в сообщение от клиента номер порта, по которому запрашиватеся соединение, например:
{'action': 'presence', 'time': 1634873801.598524, 'port': 9000, 'user': {'account_name': 'Guest'}}
"""

import socket
import argparse
import json
import time
import server_statuses as status
from server_handlers import ACTION
from server_exceptions import WrongMethod


def parse_message(data, client):
    try:
        msg = json.loads(data.decode('ascii'))
        act = msg['action']
        try:
            method = ACTION[act]
        except KeyError as e:
            raise WrongMethod(e)
        method(msg, client)
        return
    except json.decoder.JSONDecodeError:
        res = status.http_400_parse_error()
    except KeyError as e:
        res = status.http_400_param_error(e)
    except WrongMethod as e:
        res = status.http_400_method_param(e)

    client.send(json.dumps(res).encode('ascii'))



parser = argparse.ArgumentParser()
parser.add_argument('-p', type=int, default=7777, help='server port', required=False)
parser.add_argument('-a', type=str, default='', help='server address', required=False)
arg = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((arg.a, arg.p))
s.listen(5)

print(f'Сервер запущен по порту {arg.p} для \'{arg.a}\'')

try:
    while True:
        client, addr = s.accept()
        print("Получен запрос на соединение от %s" % str(addr))
        data = client.recv(4096)
        parse_message(data, client)
        client.close()
finally:
    s.close()
