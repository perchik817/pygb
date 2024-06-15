# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество
# раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить
# его как есть. Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
transformation = lambda v: v
# or solve by func
# def transformation(v): return v
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(transformation, values))
if values == transformed_values:
	print("OK, transformed")
else:
	print("Failed to transform")


# import random as r
# numbers = [r.randint(1, 100) for i in range(5)]
# is_odd = lambda x: x % 2 == 1
# sorted_nums = filter(is_odd, numbers)
#
# nums = [2, 4, 6, 8, 10, 12]
# carbons = [58, 46, 34, 22, 10, 8]
# union = []
# for n1, n2 in zip(nums, carbons):
# 	union.append(n1 + n2)
# print(union)
#
# from math import factorial
# elem = [1, 2, 3, 4, 5, 6, 7, 8]
# nums_factorials = list(map(factorial, elem))
# print(nums_factorials)