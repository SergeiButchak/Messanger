"""
Задание 2.
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
автоматизирующий его заполнение данными. Для этого:
    a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
    цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
    orders.json. При записи данных указать величину отступа в 4 пробельных символа;

    b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого
    параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding='utf-8') as fl:
        data = json.loads(fl.read())

    data['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})

    with open('orders.json', 'w', encoding='utf-8') as fl:
        json.dump(data, fl, indent=4, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    write_order_to_json('Марк Лутц – Изучаем Python', '1', '3200', 'Иванов', '22.10.2021')
    write_order_to_json('Р. Митчелл. Скрапинг веб-сайтов с помощью Python', '1', '1500', 'Иванов', '22.10.2021')
