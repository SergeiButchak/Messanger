"""
Задание 2.
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

s_1 = b'attribute'
s_2 = b'класс'
s_3 = b'функция'
s_4 = b'type'

#     File "/home/sergey/projects/PycharmProjects/Messanger/Lesson_1/Task_1_3.py", line 7
#         s_2 = b'класс'
#            ^
# SyntaxError: bytes can only contain ASCII literal characters.

#   File "/home/sergey/projects/PycharmProjects/Messanger/Lesson_1/Task_1_3.py", line 8
#     s_3 = b'функция'
#            ^
# SyntaxError: bytes can only contain ASCII literal characters.
