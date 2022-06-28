# lambda аргументы : возвращаемое выражение
# lambda x, y: x + y

txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

# реализация через цикл for
lst = []
for s in txt:
    if 'anonymous' in s:
        lst.append((True, s))
    else:
        lst.append((False, s))
print(lst)


# реализация через map
def check_anonymous (s):
    if 'anonymous' in s:
        return True
    else:
        return False


mapping = map(lambda s: (check_anonymous(s), s), txt)
lst_2 = list(mapping)
print(lst_2)


# Однострочник
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
print(list(mark))
