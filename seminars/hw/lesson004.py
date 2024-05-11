# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# set1 = set(map(int, var2.split()))
# set2 = set(map(int, var3.split()))
# intersection = sorted(set1.intersection(set2))

# print(" ".join(map(str, intersection)))


def assembly_module(arr):
    max_sum = 1
    for i in range(len(arr) - 1):
        els_sum = arr[i - 1] + arr[i] + arr[i + 1]
        if els_sum > max_sum:
            max_sum = els_sum
    return max_sum
arr = [5, 8, 6, 4, 9, 2, 7, 3]
print(assembly_module(arr))
