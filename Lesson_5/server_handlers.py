import json
import time
import server_statuses as status


def authenticate(data, client):
    pass


def presence(data, client):

    res = status.http_200(f'{data["user"]["account_name"]} has joined to the server')
    msg = json.dumps(res, ensure_ascii=False)
    client.send(msg.encode('ascii'))


def quit_server(data, client):

    res = status.http_200(f'{data["user"]["account_name"]} has left the server')
    msg = json.dumps(res, ensure_ascii=False)
    client.send(msg.encode('ascii'))


def join_chat(data, client):
    pass


def leave_chat(data, client):
    pass


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