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
def recurs(array):
    count = 0
    if len(array) <= 2:
        return 0
    if array[0] < array[1] and array[2] < array[1]:
        count += 1
    return count + recurs(array[1:])
print(recurs([1, 3, 1, 4, 2, 3, 1]))

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся
# на разных строках.
# N = int(input("Enter a number of elements: "))
# numbers = {}
# pairs = 0
# for i in range(N):
# 	number = int(input("Enter a number: "))
# 	if number in numbers:
# 		numbers[number] += 1
# 	else:
# 		numbers[number] = 1
# for counter in numbers.values():
# 	pairs += counter // 2
# print(f"count of pairs: {pairs}")


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая
# само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары
# дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не
# превосходящее 10^5. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары
# необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).
def sum_of_divisors(n):
    divisor_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Проверяем, что это не квадратный корень
                divisor_sum += n // i
    return divisor_sum
def find_friendly_numbers(k):
    friendly_pairs = []
    for n in range(2, k + 1):
        m = sum_of_divisors(n)
        if m <= k and n != m and sum_of_divisors(m) == n and (m, n) not in friendly_pairs:
            friendly_pairs.append((n, m))
    return friendly_pairs
k = int(input("Введите число k: "))
friendly_pairs = find_friendly_numbers(k)
for pair in friendly_pairs:
    print(*pair)
  