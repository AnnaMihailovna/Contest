# Ввод чисел N, M, Q
N, M, Q = map(int, input().split())

# Ввод названий колонок
column_names = input().split()

# Словарь для хранения значений колонок
columns = {}
for i, name in enumerate(column_names):
    columns[name] = i

# Ввод элементов таблицы
table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

# Список для хранения индексов строк, удовлетворяющих всем ограничениям
valid_rows = []

# Ввод ограничений и проверка каждой строки
for _ in range(Q):
    query = input().split()

    column_name = query[0]
    operator = query[1]
    value = int(query[2])

    column_index = columns[column_name]

    # Проверка каждой строки таблицы
    for i in range(N):
        if operator == '<':
            if table[i][column_index] < value:
                valid_rows.append(i)
        elif operator == '>':
            if table[i][column_index] > value:
                valid_rows.append(i)

# Подсчет суммы чисел в строках, удовлетворяющих всем ограничениям
sum_of_valid_rows = 0
for i in valid_rows:
    sum_of_valid_rows += sum(table[i])

# Вывод результата
print(sum_of_valid_rows)
