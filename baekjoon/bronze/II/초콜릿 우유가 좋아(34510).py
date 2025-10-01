a, b, c = map(int, input().split())
n = int(input())
print(c * n + b * (-~n // 2) + a * (n % 2))
