"""
    Поиск абсолютного значения

    Нам важен только модуль отклонения, а не его знак.
    Это и называется абсолютным значением.
    Функция библиотеки NumPy в листинге 3.26 создает новый массив NumPy, содержащий модули значений исходного массива.

    Функция np.abs() преобразует отрицательные значения массива NumPy в соответствующие им положительные.
"""

import numpy as np

a = np.array([1, -1, 2, -2])

print(a)
print(np.abs(a))