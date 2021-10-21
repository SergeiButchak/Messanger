"""
Задание 1.
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
    a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
    данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения
    параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра
    поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list,
    os_code_list, os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
    main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
    «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить
    в файл main_data (также для каждого файла);

    b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
    данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;

    c. Проверить работу программы через вызов функции write_to_csv().
"""
import os
import re
import csv


def get_data():
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    file_list = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if re.match(r'^info_\d+\.txt$', f)]
    for file_name in file_list:
        with open(file_name, 'r', encoding='1251') as file:
            buf = file.readlines()
            for line in buf:
                r = re.search(r'^Изготовитель системы:[ ]*(.*)$', line)
                if r:
                    os_prod_list.append(r.group(1))
                    continue
                r = re.search(r'^Название ОС:[ ]*(.*)$', line)
                if r:
                    os_name_list.append(r.group(1))
                    continue
                r = re.search(r'^Код продукта:[ ]*(.*)$', line)
                if r:
                    os_code_list.append(r.group(1))
                    continue
                r = re.search(r'^Тип системы:[ ]*(.*)$', line)
                if r:
                    os_type_list.append(r.group(1))
                    continue
    main_data.extend(list(map(lambda a, b, c, d: [a, b, c, d], os_prod_list, os_name_list, os_code_list, os_type_list)))

    return main_data

def write_to_csv(filepath):
    data = get_data()

    dir_, filename = os.path.split(filepath)

    os.makedirs(dir_, exist_ok=True)

    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), dir_, filename)

    with open(filepath, 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        writer.writerows(data)


if __name__ == '__main__':
    write_to_csv('source_data/new_data_report.csv')
