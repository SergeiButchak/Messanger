"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

strs = [b'class', b'function', b'method']

for s in strs:
    print('*' * 40)
    print(s)
    print(type(s))
    print(' '.join(map(lambda x: f'0x{x:X}', s)))
    print(len(s))
