"""
    x.reshape((a,b)), — которая преобразует массив NumPy x в новый массив NumPy с a строк и b столбцов
    (то есть формы (a,b)).
"""

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a.reshape((2, 3)))

print(a.reshape((2, -1)))  # "-1" указывает, что numpy сам разделит на равные части.
