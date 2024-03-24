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
# a=3
# b=2
# c=4
# if c <= a * b and (c % a == 0 or c % b == 0):
#     print("yes")
# else:
#     print("no")


# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
# Пример:
# n = 385916 -> yes
# n = 123456 -> no
n = int(input("Введите шестизначный номер билета: "))
count=0
first_three_digits_sum=0
last_three_digits_sum=0
while n>0:
    digit=n%10
    count+=1
    if count <=3:
        first_three_digits_sum+=digit
    else:
        last_three_digits_sum+=digit
    n//=10
if first_three_digits_sum == last_three_digits_sum:
    print("yes")
else:
    print("no")