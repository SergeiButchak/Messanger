import json
import time
import inspect
import logging
from functools import wraps
import server_statuses as status
import log.server_log_config


def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        logger = logging.getLogger('server')
        upper_func = inspect.stack()[1][3]
        logger.info(f'Вызов функции {func.__name__} из {upper_func}')
        logger.debug(f'Функция {func.__name__}, args:{args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return call


@log
def authenticate(data, client):
    pass


@log
def presence(data, client):

    res = status.http_200(f'{data["user"]["account_name"]} has joined to the server')
    msg = json.dumps(res, ensure_ascii=False)
    client.send(msg.encode('ascii'))


@log
def quit_server(data, client):

    res = status.http_200(f'{data["user"]["account_name"]} has left the server')
    msg = json.dumps(res, ensure_ascii=False)
    client.send(msg.encode('ascii'))


@log
def join_chat(data, client):
    pass


def leave_chat(data, client):
    pass


@log
def send_message(data, client):
    pass


ACTION = {
    # "authenticate": authenticate,
    "presence": presence,
    "quit": quit_server,
    # "join": join_chat,
    # "leave": leave_chat,
    # "msg": send_message,
}