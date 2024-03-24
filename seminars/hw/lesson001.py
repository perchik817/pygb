#from autotests
# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.
# Пример:
# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)

# n = 123
# first_digit = n//100
# second_digit=(n//10)%10
# third_digit=n%10
# res =first_digit+second_digit+third_digit
# print(f"n = {n} -> res = {res} ({first_digit} + {second_digit} + {third_digit})")



# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). Выведите yes или no соответственно.
# Пример:
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no
a=3
b=2
c=4
if c <= a * b and (c % a == 0 or c % b == 0):
    print("yes")
else:
    print("no")