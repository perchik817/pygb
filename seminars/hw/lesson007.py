def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return

    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            row.append(str(operation(i, j)))
        print(" ".join(row))
print_operation_table(lambda x, y: x * y, 3, 3)
