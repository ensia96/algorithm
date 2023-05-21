n = int(input())
A = input()
s, t = A.count('s'), A.count('t')
for i in range(n):
    S = A[i] == 's'
    s-t or exit(print(A[i:]))
    s -= S
    t += ~-S
