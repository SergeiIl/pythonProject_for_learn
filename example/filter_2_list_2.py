"""
    Фильтрация двумерных массивов с помощью булева доступа по индексу
"""

import numpy as np

# Данные: популярные учетные записи Instagram (миллионы подписчиков)
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

# bool_massive = inst[:, 0].astype(float) > 100 (проводим булевой анализ)
# superstars = inst[bool_massive, 1] // выводим имена пользователей (по индексу)

# Однострочник
superstars = inst[inst[:,0].astype(float) > 100, 1]

print(superstars)

