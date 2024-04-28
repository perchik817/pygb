from quick_sort import quick_sort
import merge_sort as ms
# делим на 2 массив , пока не останется 1 элемент
nums = [12, 35, 57, 33, 4, 56, 3, 54, 68, 909, 5, 78, 0]
print(quick_sort(nums))
print(ms.merge_sort(nums))


# def fib(n):
#     if n in [1, 2]: # basis
#         return 1
#     return fib(n - 1) + fib(n - 2)


# fib_list = [fib(i) for i in range(1, 10)]
# print(fib_list)


# from modul1 import max1
# # import modul1 as m1
# # from modul1 import *
# print(max1(10,9))

# def sum_str(*args): # * means that there are infinite num of arguments
#       result = ""
#       for item in args:
#             result+=item
#       return result

# print(sum_str('q', 'w', 'e'))
# print(sum_str('q', 'w', 'r', 't'))
