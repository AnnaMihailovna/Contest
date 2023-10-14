# хитрый шифр
answer = []
n = int(input())
for i in range(n):
    data = list(input().split(','))
    simbol = len(set(data[0] + data[1] + data[2]))
    day = sum(int(i) for i in list(data[3]))
    month = sum(int(i) for i in list(data[4]))
    two = (day + month)*64
    alf = (ord(data[0][0].lower()) - ord('a') + 1)*256
    cipher = simbol + two + alf
    hex_cipher = hex(cipher).upper()
    answer.append(hex_cipher)

for i in answer:
    print(i[-3:].rjust(3, '0'), end=' ')
