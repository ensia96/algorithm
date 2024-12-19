i = int(1e6)
n = p = i
m = q = -i
for _ in " " * int(input()):
    x, y, d = input().split()
    if d == "L":
        n = min(n, int(x))
    if d == "R":
        m = max(m, int(x))
    if d == "U":
        q = max(q, int(y))
    if d == "D":
        p = min(p, int(y))
print([(n - m - 1) * (p - q - 1), "Infinity"][n == p == i or m == q == -i])
