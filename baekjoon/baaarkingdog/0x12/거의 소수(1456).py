a, b = map(int, input().split())
A, c = 0, int(b**.5)
d = [1]*(c+1)
for i in range(2, c+1):
    if not d[i]:
        continue
    t = i*i
    while t <= b:
        A, t = A+(a <= t), t*i
    for j in range(i+i, c+1, i):
        d[j] = 0
print(A)
