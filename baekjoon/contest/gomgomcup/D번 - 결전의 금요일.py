n = int(input())
A = [*map(int, input().split())]
D = [0]
for i in range(n):
    D += D[i]+A[i],
for i in range(n+1):
    for j in range(i):
        (1+D[i]-D[j]) % 7 == 5 and exit(print('YES'))
print('NO')
