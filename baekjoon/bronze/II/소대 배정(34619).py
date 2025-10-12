a, b, n, k = map(int, input().split())
x = ~-k // n
print(1 + x // b, 1 + x % b)
