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
# l = [1, 2, 3, 4, 5]
# k = 3

# def shift_list(l1, k):
#     size = len(l1)
#     list_l = list()
#     for i in range(size):
#         ind = (i + k) % size
#         list_l.append(l1[ind])
#     return list_l

# shifted_list_k = shift_list(l, k)
# print(shifted_list_k)


# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
def get_unique_values(list_of_dicts):
    unique_values = set()
    for d in list_of_dicts:
        for value in d.values():
            unique_values.add(value.strip())  # Removing leading and trailing whitespace
    return unique_values

list_of_dicts = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": " S005 "},
    {" V ": " S009 "},
    {" VIII ": " S007 "},
]

unique_values = get_unique_values(list_of_dicts)
print(unique_values)
