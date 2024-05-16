# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
def fib(n):
    if n <= 1 and n >= (-1):
        return n
    if n < 0:
        return (-1) * (fib(n + 1) - fib(n + 2))
    return fib(n - 1) + fib(n - 2)
print(fib(-2))
