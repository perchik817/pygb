# список - упорядоченный конечный набор элементов
# list1 = []
# list1 = list()
# list1 = [1, 2, 3, 4]

# for item in list1:
#     print(item)

# print(len(list1))

# list1.append(8)
# print(*list1)  # * to see without brackets

# print(list1.pop())  # delete the last element
# print(list1.pop(1))  # remove the second element
# print(list1.insert(1, 325))  # insert the element as second

# print(list1[:])  # print elements from the start of list1 till the end
# print(list1[::6])  # print elements from the start of list1 till the end with step = 6


# кортеж - неизменяемый список. занимает меньше места в памяти и работает быстрее
# tup = tuple(list1)  # can't be changed, after each el must be comma
# print(tup)
# a, b, c, d = tup  # unwrap tuple
# print(a, b, c, d)


# словари - неупорядоченные коллекции (ключ -значение)
# d = {}
# d = dict()
# d["q"] = "qwerty"
# d["w"] = "qwerty"
# d["e"] = "qwerty"
# d["r"] = "qwerty"
# d["t"] = "qwerty"
# d["y"] = "qwerty"

# for item in d:
#     print("{}: {}".format(item, d[item]))
# for k, v in d.items():
#     print(k, v)


# # множества - не упорядочены, уникальные элементы
# colors = {'red', 'green', 'blue'}
# colors.add('white')
# print(colors)
# colors.remove('white')
# print(colors)
# colors.discard('white') # проверяет наличие эдемента в множ. если есть - удаляет, нет - пропускает строку и не выдает ошибку
# colors.clear()
# print(colors)

# q = set()

# # Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}

# # Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


l = [i for i in range(1, 28) if i % 2 == 0]
print(l)

l2 = [(i, i + 8) for i in range(1, 28) if i % 2 != 0]
print(l2)
