import json
import select
import time
import inspect
import logging
from functools import wraps
import server.server_statuses as status
from server.server_exceptions import WrongMethod
import log.server_log_config

logger = logging.getLogger('server')


def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        upper_func = inspect.stack()[1][3]
        logger.info(f'Вызов функции {func.__name__} из {upper_func}')
        logger.debug(f'Функция {func.__name__}, args:{args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return call


def parse_message(data, conn, clients):
    try:
        msg = json.loads(data.decode('ascii'))
        act = msg['action']
        try:
            method = ACTION[act]
        except KeyError as e:
            raise WrongMethod(e)
        method(msg, conn, clients)
        return
    except json.decoder.JSONDecodeError:
        res = status.http_400_parse_error()
    except KeyError as e:
        res = status.http_400_param_error(e)
    except WrongMethod as e:
        res = status.http_400_method_param(e)
    logger.info(f'При обработке запроса произошла ошибка: {res["error"]}')
    conn.send(json.dumps(res).encode('ascii'))


@log
def authenticate(data, conn,clients):
    pass


@log
def presence(data, conn, clients):

    res = status.http_200(f'{data["user"]["account_name"]} has joined to the server')
    msg = json.dumps(res, ensure_ascii=False)
    conn.send(msg.encode('ascii'))

    send_data_list = []
    try:
        if clients:
            r, send_data_list, e = select.select([], clients, [], 0)
    except OSError:
        pass
    if send_data_list:
        msg_txt = status.client_message('server', f'{data["user"]["account_name"]} has joined to the server')
        msg = json.dumps(msg_txt, ensure_ascii=False)
        for s in send_data_list:
            try:
                s.send(msg.encode('ascii'))
            except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                logger.info(f'Соединение с сервером {s} было потеряно.')
                clients.remove(s)


@log
def quit_server(data, conn, clients):

    res = status.http_200(f'{data["user"]["account_name"]} has left the server')
    msg = json.dumps(res, ensure_ascii=False)
    conn.send(msg.encode('ascii'))


@log
def join_chat(data, conn, clients):
    pass


def leave_chat(data, conn, clients):
    pass


@log
def send_message(data, conn, clients):
    send_data_list = []
    try:
        if clients:
            r, send_data_list, e = select.select([], clients, [], 0)
    except OSError:
        pass
    if send_data_list:
        user = data['account_name']
        text = data['mess_text']
        msg_txt = status.client_message(user, text)
        msg = json.dumps(msg_txt, ensure_ascii=False)
        for s in send_data_list:
            try:
                s.send(msg.encode('ascii'))
            except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                logger.info(f'Соединение с сервером {s} было потеряно.')
                clients.remove(s)


ACTION = {
    # "authenticate": authenticate,
    "presence": presence,
    "quit": quit_server,
    # "join": join_chat,
    # "leave": leave_chat,
    "message": send_message,
}