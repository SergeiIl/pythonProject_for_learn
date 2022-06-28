"""
    Создание расширенных фильтров массивов с помощью статистических показателей,
    а также математических и логических операций.

    Обнаружение аномальных значений: наблюдаемое значение считается аномальным (outlier),
    если отличается от среднего более чем на стандартное отклонение.

    Показатель отказов (bounce rate) — это процент посетителей,
    которые уходят с сайта сразу же после посещения одной страницы.
"""

import numpy as np
import matplotlib.pyplot as plt
sequence = np.random.normal(10.0, 1.0, 500)
#print(sequence)
plt.xkcd()
plt.hist(sequence)
plt.annotate(r"$\omega_1=9$", (9, 70))
plt.annotate(r"$\omega_2=11$", (11, 70))
plt.annotate(r"$\mu=10$", (10, 90))
# plt.savefig("plot.jpg")
plt.show()
