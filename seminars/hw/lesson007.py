def has_rythm(s):
	d = {}
	for subs in s.split():
		vowels_count = sum(1 for i in subs if i in "аеоуыяиюёэ")
		d[subs] = vowels_count
	
	v = set(d.values())
	return len(v) == 1

def subs_count(s):
	return len(s.split())

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'  # Парам пам-пам
# stroka = "мо-локо и мёд" # Пам парам
stroka = "одна-фраза" # Количество фраз должно быть больше одной!

if subs_count(stroka) > 1:
	if has_rythm(stroka):
		print("Парам пам-пам")
	else:
		print("Пам парам")
else:
	print("Количество фраз должно быть больше одной!")


# def print_operation_table(operation, num_rows=9, num_columns=9):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#
#     for i in range(1, num_rows + 1):
#         row = []
#         for j in range(1, num_columns + 1):
#             row.append(str(operation(i, j)))
#         print(" ".join(row))
# print_operation_table(lambda x, y: x * y, 3, 3)
