n = int(input())
f, s = 0, 1
while n > 0:
    f += 1
    s += f * 4
    n -= s
print(f)
