import time


def http_400_parse_error():
    res = dict()
    res['response'] = 400
    res['time'] = time.time()
    res['error'] = 'JSON cannot parse message'

    return res


def http_400_param_error(param):
    res = dict()
    res['response'] = 400
    res['time'] = time.time()
    res['error'] = f'Mandatory parameter {param} is missing'

    return res


def http_400_method_param(param):
    res = dict()
    res['response'] = 400
    res['time'] = time.time()
    res['error'] = f'Unrecognized method {param}'

    return res


def http_200(msg):
    res = dict()
    res['response'] = 200
    res['time'] = time.time()
    res['alert'] = f'{msg}'

    return res


def client_message(user, msg):
    res = dict()
    res['action'] = 'message'
    res['time'] = time.time()
    res['account_name'] = user
    res['mess_text'] = msg

    return res