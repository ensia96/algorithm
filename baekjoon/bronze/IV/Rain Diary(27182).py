n, m = map(int, input().split())
for x in [28, 29, 30, 31]:
    a, b = (n-7+x) % x, (m+7+x) % x
    a-b or print(a)
