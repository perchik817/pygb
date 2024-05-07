import os
print(os.getcwd())
print(os.path.abspath("file.txt"))


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#       print(line)
# data.close()

# with open("file.txt", "w") as data:
#     data.write("line 1\n")
#     data.write("line 2\n")

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)


# users = ["user1", "user2", "user3", "user4", "user5"]
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list(filter(lambda x: x  % 10 == 5, data))
# print(res)


# data = "35 67 2 78 57 89 95 57 6"
# data = list(map(int, data.split()))
# print(data)


# list1 = [x for x in range(1, 5)]
# print(list1)
# list1 = list(map(lambda x: x + 10, list1))
# print(list1)


# data = [i for i in range(1, 18)]
# res = list()
# for item in data:
#     if item % 2 == 0:
#         res.append((item, item**2))
# print(res)

## select(f, col) is equal to method map(f, o)
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# print(res)  # [2, 8, 38]
# res = list(select(lambda x: (x, x**2), res))
# print(res)


# def math(op, x, y):
#     print(op(x, y))
# calc = lambda a, b: a + b
# math(calc, 45, 3)
