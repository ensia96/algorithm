input()
y = m = 0

for t in map(int, input().split()):
    y += (t // 30 + bool(t % 30)) * 10
    m += (t // 60 + bool(t % 60)) * 15

a = min(y, m)

print(*[*[s for c, s in ((y, "Y"), (m, "M")) if c == a], a])
