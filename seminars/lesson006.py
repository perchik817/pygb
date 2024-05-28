# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# def array1_minus_array2(a1, a2):
# 	result = [item for item in a1 if item not in set(a2)]
# 	return result
# n = int(input("Enter the number of elements in first array: "))
# arr1 = [int(input()) for i in range(n)]
# m = int(input("Enter the number of elements in second array: "))
# arr2 = [int(input()) for j in range(m)]
# print(
# 	f"array 1: {arr1}"
# 	f"\narray2: {arr2}"
# 	f"\narray1 - array2: {array1_minus_array2(arr1, arr2)}"
# 	)


# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество
# элементов в массиве. Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# N = int(input("Enter the number of elements in array: "))
# array = [int(input()) for i in range(N)]
# count = 0
# for i in range(1, N - 1):
# 	if array[i - 1] < array[i] and array[i + 1] < array[i]:
# 		count += 1
# print(count)


# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся
# на разных строках.
N = int(input("Enter a number of elements: "))
numbers = {}
pairs = 0
for i in range(N):
	number = int(input("Enter a number: "))
	if number in numbers:
		numbers[number] += 1
	else:
		numbers[number] = 1
for counter in numbers.values():
	pairs += counter // 2
print(f"count of pairs: {pairs}")