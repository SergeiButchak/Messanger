import json
import inspect
import logging
from functools import wraps
from common.colorcon import colors
from client.client_exceptions import WrongMethod
import client.client_statuses as status
import log.client_log_config

logger = logging.getLogger('client')
text_attr = colors()

def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        upper_func = inspect.stack()[1][3]
        logger.info(f'Вызов функции {func.__name__} из {upper_func}')
        logger.debug(f'Функция {func.__name__}, args:{args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return call


def parse_message(data, conn):
    try:
        msg = json.loads(data.decode('ascii'))
        if 'action' in msg:
            act = msg['action']
            try:
                method = ACTION[act]
            except KeyError as e:
                raise WrongMethod(e)
            method(msg, conn)
        return
    except json.decoder.JSONDecodeError:
        res = status.http_400_parse_error()
    except KeyError as e:
        res = status.http_400_param_error(e)
    except WrongMethod as e:
        res = status.http_400_method_param(e)
    logger.info(f'При обработке запроса произошла ошибка: {res["error"]}')
    conn.send(json.dumps(res).encode('ascii'))


def message(data, conn):

    user = data['account_name']
    text = data['mess_text']
    if user == 'server':
        text_color = text_attr.C_YELLOW
        user_txt = ''
    else:
        text_color = text_attr.C_GREEN
        user_txt = f'{text_color}{text_attr.UNDERL}{user}{text_attr.RESET}: '

    print(f'{user_txt}{text_color}{text}{text_attr.RESET}')


ACTION = {
    # "authenticate": authenticate,
    # "presence": presence,
    # "quit": quit_server,
    # "join": join_chat,
    # "leave": leave_chat,
    "message": message,
}