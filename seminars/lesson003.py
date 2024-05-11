# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
l = [1, 1, 2, 0, -1, 3, 4, 4]
def count_different_numbers(l):
    return len(set(l))

print(count_different_numbers(l))

