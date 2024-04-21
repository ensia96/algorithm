n, l, d = map(int, input().split())
t = 0
for i in range(n):
    t += l
    for j in range(5):
        t += 1
        t % d < 1 or exit(print(t))
print(t)
