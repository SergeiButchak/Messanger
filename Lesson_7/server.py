import logging
import select
import socket
import argparse
from server.server_handlers import parse_message

logger = logging.getLogger('server')


def new_socket(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((address, port))
        s.listen(5)
        s.settimeout(0.5)
        return s
    except OSError as e:
        logger.info(f'{e} on {address}:{port}')
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, default=7777, help='server port', required=False)
    parser.add_argument('-a', type=str, default='', help='server address', required=False)
    arg = parser.parse_args()

    s = new_socket(arg.a, arg.p)

    if s is None:
        exit()

    clients = []
    logger.info(f'Сервер запущен по порту {arg.p} для \'{arg.a}\'')

    while True:
        try:
            client, client_address = s.accept()
        except OSError:
            pass
        else:
            logger.info(f'Установлено соединение с ПК {client_address}')
            clients.append(client)

        recv_data_list = []
        send_data_list = []
        err_list = []

        try:
            if clients:
                recv_data_list, send_data_list, err_list = select.select(clients, clients, [], 0)
        except OSError:
            pass

        if recv_data_list:
            for r in recv_data_list:
                try:
                    data = r.recv(1024)
                    parse_message(data, r, clients)
                except:
                    clients.remove(r)



    # try:
    #     while True:
    #         try:
    #             conn, addr = s.accept()
    #         except OSError as e:
    #             pass
    #         else:
    #             logger.info(f'Получен запрос на соединение от {addr}')
    #             clients.append(conn)
    #             data = conn.recv(4096)
    #         finally:
    #             recv_data_lst = []
    #             send_data_lst = []
    #             try:
    #                 recv_data_lst, send_data_lst, e = select.select(clients, clients, [], 0)
    #             except Exception as e:
    #                 pass
    #
    #             if recv_data_lst:
    #                 for r in recv_data_lst:
    #                     try:
    #                         data = r.recv(4096)
    #                         logger.debug(f'Данные от клиента {r}: {data.decode()}')
    #                         parse_message(data, r, send_data_lst)
    #                     except ConnectionResetError as e:
    #                         logger.error(e)
    #
    # finally:
    #     s.close()


if __name__ == '__main__':
    main()