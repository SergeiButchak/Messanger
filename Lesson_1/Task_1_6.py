"""
Задание 6.
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое
"""

with open('test_file.txt', 'rb') as fl:
    s = fl.read()
    print(s)

with open('test_file.txt', encoding='utf-8', errors='replace') as fl:
    print(fl.read())
