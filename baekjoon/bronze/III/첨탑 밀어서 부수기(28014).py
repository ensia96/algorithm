input()
p = t = 0
for c in map(int, input().split()):
    t += c >= p
    p = c
print(t)
