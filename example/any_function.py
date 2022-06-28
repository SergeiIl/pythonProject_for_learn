"""
    Поиск компаний, платящих меньше минимальной зарплаты, с помощью выражений-генераторов.

    Функция any() языка Python, принимающая на входе итерируемый объект, например,
    список, и возвращающая True, если вычисление хотя бы одного элемента этого итерируемого объекта дает True.
"""

companies = {
    'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
    'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
    'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}}


# Полное решение
def check_illegal (data):
    for y in companies[x].values():
        if y < 9:
            return y


lst = []
for x in companies:
    if check_illegal(companies):
        lst.append(x)
print(lst)

# Однострочник
illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]

print(illegal)