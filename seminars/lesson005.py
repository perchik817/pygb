# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
# def fib(n):
#     if n <= 1 and n >= (-1):
#         return n
#     if n < 0:
#         return (-1) * (fib(n + 1) - fib(n + 2))
#     return fib(n - 1) + fib(n - 2)
# print(fib(-2))


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# marks_str = "1 3 3 3 4".split()
# marks_list = [int(mark) for mark in marks_str]
# max_mark = max(marks_list)
# min_mark = min(marks_list)
# hacked_marks_list = [min_mark if mark == max_mark else mark for mark in marks_list]
# print(f"hacked marks: {hacked_marks_list}")


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
def primary_num(num):
      for i in range(2, num):
            if num % i == 0:
                  return False
      if num == 1:
            return True
      return True
num = int(input("Enter a number: "))
if primary_num(num):
      print("yes")
else:
      print("no")