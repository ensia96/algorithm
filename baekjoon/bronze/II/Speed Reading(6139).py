n, k = map(int, input().split())
for _ in " " * k:
    a, b, c = map(int, input().split())
    a = -(n // -a)
    t = a % b
    print((a // b) * (b + c) + t - c * (t < 1))
