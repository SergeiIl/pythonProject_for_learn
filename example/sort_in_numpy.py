"""
    Сортировка — центральный элемент более сложных приложений, таких как коммерческие расчеты,
    планирование процессов в операционных системах (очереди по приоритету) и поисковые алгоритмы.

    Функции sort() и argsort() в в NumPy
"""

import numpy as np

a = np.array([10, 6, 8, 2, 5, 4, 9, 1])
print(np.sort(a))  # возвращает отсортированные значения

print(np.argsort(a))  # возвращает индексы отсортированных значений

b = np.array([[1, 6, 2],
              [5, 1, 1],
              [8, 0, 1]])

print(np.sort(b, axis=0))

print(np.sort(b, axis=1))
