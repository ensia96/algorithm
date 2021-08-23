a, b, c = map(int, input().split())

if a == b or c == a or b == c:
    r = 1000 + (a if a == b or c == a else b) * 100
    if a == b == c:
        r *= 10
    print(r)
else:
    print(max(a, b, c) * 100)
