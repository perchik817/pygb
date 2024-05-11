# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

string = input("enter satze: ").split()
d = dict()
result = list()
for i in string:
    if i in d.keys():
        result.append(f"{i}_{d[i]}")
        d[i] += 1
    else:
        result.append(i)
        d[i] = 1
print(*result)
print(d)
