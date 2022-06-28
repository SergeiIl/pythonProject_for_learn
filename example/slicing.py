"""
Срез (slicing) — процесса «вырезания» подпоследовательности из исходной полной последовательности —
для обработки простых текстовых запросов.
x[начало:конец:шаг]
"""

# s = 'Eat more fruits!'
#
# # если начало>=конец с положительным значением шаг, то срез будет пустым
# print(s[0:3])
# print(s[3:0])
# print(s[:5])
# print(s[5:])
#
# # если аргумент конец больше длины последовательности, то Python вырезает все элементы последовательности вплоть до
# # крайнего справа элемента включительно
# print(s[:100])
# print(s[4:8:2])
#
# # если шаг больше нуля, то по умолчанию начало среза — крайний слева элемент, а конец — крайний справа (включительно)
# print(s[::3])
#
# # если шаг меньше нуля, то срез обходит последовательность в обратном порядке
# print(s[::-1])
# print(s[6:1:-1])


letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''
# Однострочник
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1
# Результат
print(find(letters_amazon, 'SQL'))