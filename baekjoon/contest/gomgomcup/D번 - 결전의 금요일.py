def f(x):
    if x % 7 == 4:
        exit(print('YES'))
    for i in range(1, 7):
        if C[i]:
            C[i] -= 1
            f(x+i)
            C[i] += 1


n = int(input())
A = [*map(int, input().split())]
C, c = [0]*7, 0
for a in A:
    if a % 7:
        C[a % 7] += 1
        c += 1
f(0+4*bool(C[4]+(c > 5)))
print('NO')
