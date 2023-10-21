N, M, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diversity_indicator = []

for i in range(Q):
    type, player, card = input().split()
    card = int(card)
    if type == '1':
        if player == 'A':
            A.append(card)
        else:
            B.append(card)
    else:
        if player == 'A':
            A.remove(card)
        else:
            B.remove(card)
    for i in A:
    	if i in B:
            A.remove(i)
            B.remove(i)

print(' '.join(map(str, diversity_indicator)))