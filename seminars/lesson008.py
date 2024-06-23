# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки,
# которую необходимо перенести из одного файла в другой.

import os.path

def get_all_data(file):
	if not os.path.exists(file):
		print("Файл не найден.")
		return
	with open(file, 'r') as contacts:
		readAll = contacts.read()
		print(readAll)

def write_data(file):
	last_name = input("Введите фамилию: ")
	name = input("Введите имя: ")
	middle_name = input("Введите отчество: ")
	phone_number = input("Введите номер телефона: ")
	with open(file, 'a') as contacts:
		contacts.write(
				f"Фамилия: {last_name}\n"
				f"Имя: {name}\n"
				f"Отчество: {middle_name}\n"
				f"Номер телефона: {phone_number}\n"
				f"------------------------------\n"
				)

def search_data_by_name(file, query):
	if not os.path.exists(file):
		print("Файл не найден.")
		return
	found = False
	with open(file, 'r') as contacts:
		lines = contacts.readlines()
		contact_info = ""
		for i in range(len(lines)):
			if query.lower() in lines[i].lower():
				# Найти начало контакта
				while i > 0 and "------------------------------" not in lines[i - 1]:
					i -= 1
				# Считать весь контакт
				j = i
				while j < len(lines) and "------------------------------" not in lines[j]:
					contact_info += lines[j]
					j += 1
				contact_info += lines[j]  # Добавляем строку разделителя
				print(contact_info.strip())
				contact_info = ""
				found = True
	if not found:
		print("Запись не найдена.")

def copy_line(source_file, line_number):
	target_file = "copy_file.txt"
	if not os.path.exists(source_file):
		print("Файл не найден.")
		return
	with open(source_file, 'r') as src:
		lines = src.readlines()
	if line_number < 1 or line_number > len(lines):
		print("Неверный номер строки.")
		return
	
	i = line_number - 1
	while i > 0 and "------------------------------" not in lines[i - 1]:
		i -= 1
	contact_info = ""
	j = i
	while j < len(lines) and "------------------------------" not in lines[j]:
		contact_info += lines[j]
		j += 1
	contact_info += lines[j]
	with open(target_file, 'a') as tgt:
		tgt.write(contact_info + "\n")
	
	print(f"Контакт из строки {line_number} успешно скопирован из {source_file} в {target_file}.")

file = "contacts.txt"
while True:
	print(
			"======================ТЕЛЕФОННЫЙ СПРАВОЧНИК====================="
			"\n1. Вывести все данные"
			"\n2. Сохранить данные"
			"\n3. Поиск записи по фамилии/имени"
			"\n4. Копировать данные из одного файла в другой"
			"\n5. Выход"
			"\nВыберите действие 1-5:"
			)
	try:
		choice = int(input())
	except ValueError:
		print("Неверный ввод. Пожалуйста, введите число от 1 до 5.")
		continue
	
	match choice:
		case 1:
			get_all_data(file)
		case 2:
			write_data(file)
		case 3:
			q = input("Введите фамилию или имя для поиска: ")
			search_data_by_name(file, q)
		case 4:
			line_number = int(input("Введите номер строки для копирования: "))
			copy_line(file, line_number)
		case 5:
			break
		case _:
			print("Неверный ввод")
			continue
