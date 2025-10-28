n, s = map(int, input().split())
x, t = 0, s
for _ in ' ' * n:
    a, *_ = input()
    w = int(a) + len(_)
    if w > t:
        x += 1
        t = s
    t -= w
print(x)
