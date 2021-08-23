input()
y = m = 0

for t in map(int, input().split()):
    y += (t // 30 + 1) * 10
    m += (t // 60 + 1) * 15

a = min(y, m)

print(*[*[s for c, s in ((y, "Y"), (m, "M")) if c == a], a])
