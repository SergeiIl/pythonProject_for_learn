"""
    Форматирование баз данных с помощью функции zip()
    Функция zip() принимает на входе итерируемые объекты iter_1, iter_2, ..., iter_n
    и агрегирует их в один итерируемый объект путем выстраивания соответствующих i-х значений в один кортеж.
"""

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

zipped = list(zip(lst_1, lst_2))
# print(zipped)

lst_1_new, lst_2_new = zip(*zipped)
# print(list(lst_1_new))
# print(list(lst_2_new))

column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]

# Однострочник
db = [dict(zip(column_names, row)) for row in db_rows]
print(db)
