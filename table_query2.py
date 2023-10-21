N, M, Q = map(int, input().split())
columns = input().split()

table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

valid_rows = set(range(N))

for _ in range(Q):
    query = input().split()
    column_name = query[0]
    operator = query[1]
    value = int(query[2])

    column_index = columns.index(column_name)
    if operator == '<':
        valid_rows = {i for i in valid_rows if table[i][column_index] < value}
    elif operator == '>':
        valid_rows = {i for i in valid_rows if table[i][column_index] > value}

total_sum = sum(sum(table[i]) for i in valid_rows)

print(total_sum)
