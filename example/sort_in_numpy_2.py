"""
    Сортировка — центральный элемент более сложных приложений, таких как коммерческие расчеты,
    планирование процессов в операционных системах (очереди по приоритету) и поисковые алгоритмы.

    Функции sort() и argsort() в в NumPy
"""

import numpy as np

# Данные: оценки за экзамен SAT для различных абитуриентов
sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])
# Однострочник / отсортировали список sat_scores, передали его в вызов students, по возрастанию выбрали последние 3
top_3 = students[np.argsort(sat_scores)][:-4:-1]
# Результат
print(top_3)