r, b = map(int, input().split())
for i in range(1, int(b**.5)+1):
    if not b % i:
        x, y = b//i+2, i+2
        x*y == r+b and exit(print(x, y))
