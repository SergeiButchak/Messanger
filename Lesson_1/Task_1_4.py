"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

strs = ['разработка', 'сокет', 'декоратор']
bytes_strs = []

for s in strs:
    s = s.encode()
    bytes_strs.append(s)
    print(s)

for s in bytes_strs:
    print(s.decode())
