import logging
import socket
import argparse
import json
import server_statuses as status
from server_handlers import ACTION
from server_exceptions import WrongMethod
import log.server_log_config

logger = logging.getLogger('server')

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
    logger.info(f'При обработке запроса произошла ошибка: {res["error"]}')
    client.send(json.dumps(res).encode('ascii'))



parser = argparse.ArgumentParser()
parser.add_argument('-p', type=int, default=7777, help='server port', required=False)
parser.add_argument('-a', type=str, default='', help='server address', required=False)
arg = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((arg.a, arg.p))
except OSError as e:
    logger.info(f'{e} on {arg.a}:{arg.p}')
    exit()
s.listen(5)

logger.info(f'Сервер запущен по порту {arg.p} для \'{arg.a}\'')

try:
    while True:
        client, addr = s.accept()
        logger.info(f'Получен запрос на соединение от {addr}')
        data = client.recv(4096)
        logger.debug(f'Данные от клиента {addr}: {data.decode()}')
        parse_message(data, client)
        client.close()
finally:
    s.close()
