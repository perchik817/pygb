# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# l = [1, 1, 2, 0, -1, 3, 4, 4]
# def count_different_numbers(l):
#     return len(set(l))

# print(count_different_numbers(l))


# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
l = [1, 2, 3, 4, 5]
k = 3

def shift_list(l1, k):
    size = len(l1)
    list_l = list()
    for i in range(size):
        ind = (i + k) % size
        list_l.append(l1[ind])
    return list_l

shifted_list_k = shift_list(l, k)
print(shifted_list_k)
