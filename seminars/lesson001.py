# 1-ОЕ ЗАДАНИЕ
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
# import math
# n=float(input("Сколько км проезжает машина за день? "))
# m=float(input("Какова длина маршрута в км? "))
# # day = math.ceil(m / n)
# day = int(-(-m // n)) #так как округление идет в меньшую сторону, то умножаем на -1, чтобы округление произошло меньше результата
# print(f"Нужно {day} дн.")


