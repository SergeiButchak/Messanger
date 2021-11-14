import time


def client_presence(user):
    res = dict()
    res['action'] = 'presence'
    res['time'] = time.time()
    res['user'] = dict()
    res['user']['account_name'] = user

    return res


def client_message(user, msg):
    res = dict()
    res['action'] = 'message'
    res['time'] = time.time()
    res['account_name'] = user
    res['mess_text'] = msg

    return res


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