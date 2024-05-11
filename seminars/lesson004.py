# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили
# так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.
nums = list()
while True:
    num = int(input("enter a number: "))
    if num == 0:
        break
    else:
        nums.append(num)
print(max(nums))
# max_num = 1
# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         break
#     if num > max_num:
#         max_num = num
# print(max_num)


# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# user_str = input("Enter your text: ").lower().split()
# user_str = """She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells""".lower().split()
# print(len(set(user_str)))


# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# string = input("enter satze: ").split()
# d = dict()
# result = list()
# for i in string:
#     if i in d.keys():
#         result.append(f"{i}_{d[i]}")
#         d[i] += 1
#     else:
#         result.append(i)
#         d[i] = 1
# print(*result)
# print(d)
