# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую
# большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по
# которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет
# нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары
# чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала
# вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая
# далекая планета ровно одна

from math import pi
def find_farthest_orbit1(list_of_orbits):
	ellipsis = [x for x in list_of_orbits if x[0] != x[1]]
	areas = [(pi * a * b, (a, b)) for a, b in ellipsis]
	max_area_orbit = max(areas, key = lambda x: x[0])
	return max_area_orbit[1]
def find_farthest_orbit2(list_of_orbits):
	areas = list(map(lambda x: x[0] * pi * x[1] if x[0] != x[1] else 0, list_of_orbits))
	max_area = max(areas)
	index = areas.index(max_area)
	return list_of_orbits[index]
def find_farthest_orbit3(list_of_orbits):
	return max(list_of_orbits, key = lambda x: x[0] * pi * x[1] if x[0] != x[1] else 0)
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit1(orbits))
print(*find_farthest_orbit2(orbits))
print(*find_farthest_orbit3(orbits))

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество
# раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить
# его как есть. Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# transformation = lambda v: v
# or solve by func
# def transformation(v): return v
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
# 	print("OK, transformed")
# else:
# 	print("Failed to transform")


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
