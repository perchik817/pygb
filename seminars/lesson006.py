# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
def array1_minus_array2(a1, a2):
	result = [item for item in a1 if item not in set(a2)]
	return result

n = int(input("Enter the number of elements in first array: "))
arr1 = [int(input()) for i in range(n)]
m = int(input("Enter the number of elements in second array: "))
arr2 = [int(input()) for j in range(m)]
print(
	f"array 1: {arr1}"
	f"\narray2: {arr2}"
	f"\narray1 - array2: {array1_minus_array2(arr1, arr2)}"
	)
