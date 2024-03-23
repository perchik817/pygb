# print("Enter first num: ")
# a = float(input())
# b = float(input("Enter second number: "))
# print(f"{a} * {b} = {round(a * b, 3)}")


# a = 1 < 1 < 3 < 4 < 10
# print(a)


# n = 423
# sum = 0
# if(n >= 300):
#       while n > 0:
#             x = n % 10
#             sum += x
#             n //= 10
# print(sum)


# n=int(input("enter a number: "))
# flag=True
# i=2
# while flag:
#       if n % i == 0:
#             flag=False
#             print(i)
#       elif n//2 <i:
#             print(n)
#             flag=False
#       i+=1


# line="something...is..dead"
# for i in line:
#       print(i)


text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.lower()) # съешь ещё этих мягких французских булок
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ from ind=0 till ind<2
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...