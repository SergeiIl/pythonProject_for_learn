# 1 lesson / листинг

lst = []
for x in range(3):
    for y in range(3):
        lst.append((x, y))

print(lst)

# Однострочник
print([(x, y) for x in range(3) for y in range(3)])

# print([x.lower() for x in ['I', 'AM', 'NOT', 'SHOUTING']])
# print([x ** 2 for x in range(10) if x % 2 > 0])


# 2 lesson / словарь

employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 88123,
             'Eve': 93121}

top_earners = []
for k, v in employees.items():
    if v >= 100000:
        top_earners.append((k, v))
print(top_earners)

# Однострочник
top_earners = [(k, v) for k, v in employees.items() if v >= 100000]
print(top_earners)


# 3 lesson / Поиск информативных слов с помощью спискового включения

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

lst_3 = []
for line in text.split('\n'):
    lst_3_t = []
    for x in line.split():
        if len(x) > 3:
            lst_3_t.append(x)
    lst_3.append(lst_3_t)

print(lst_3)

# Однострочник
w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

print(w)