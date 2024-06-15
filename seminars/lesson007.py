import random as r
numbers = [r.randint(1, 100) for i in range(5)]
is_odd = lambda x: x % 2 == 1
sorted_nums = filter(is_odd, numbers)

nums = [2, 4, 6, 8, 10, 12]
carbons = [58, 46, 34, 22, 10, 8]
union = []
for n1, n2 in zip(nums, carbons):
	union.append(n1 + n2)
print(union)

from math import factorial
elem = [1, 2, 3, 4, 5, 6, 7, 8]
nums_factorials = list(map(factorial, elem))
print(nums_factorials)