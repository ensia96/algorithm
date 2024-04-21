n, l, d = map(int, input().split())
t = 0
for i in range(n):
    t += l
    for j in range(5):
        t % d == 0 and exit(print(t))
        t += 1
print(t)
