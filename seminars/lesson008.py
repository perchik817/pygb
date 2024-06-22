# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
import os.path

def getAllData(file):
	if not os.path.exists(file):
		print("Файл не найден.")
		return
	with open(file, 'r') as contacts:
		readAll = contacts.read()
		print(readAll)

def writeData(file):
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
		
def searchDataByName(file, query):
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

file = "contacts.txt"
while True:
	print(
			"======================ТЕЛЕФОННЫЙ СПРАВОЧНИК====================="
			"\n1. Вывести все данные"
			"\n2. Сохранить данные"
			"\n3. Поиск записи по фамилии/имени"
			"\n4. Выход"
			"\nВыберите действие 1-4:"
			)
	try:
		choice = int(input())
	except ValueError:
		print("Неверный ввод. Пожалуйста, введите число от 1 до 4.")
		continue
	
	match choice:
		case 1:
			getAllData(file)
		case 2:
			writeData(file)
		case 3:
			q = input("Введите фамилию или имя для поиска: ")
			searchDataByName(file, q)
		case 4:
			break
		case _:
			print("Неверный ввод")
			continue
