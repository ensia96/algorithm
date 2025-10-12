a, b, n, k = map(int, input().split())
print(1 + ~-k // n // b, 1 + ~-k // n % b)
