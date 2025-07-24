n, *A = map(int, open(0))
D = [4]*12
D[10] = 16
for a in A:
    D[a] -= 1
print('DVOUSCTIA'[sum(D[i]for i in range(22-sum(A), 12))*2 < 52-n::2])
