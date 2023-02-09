a, b = map(int, input().split())
print(min(a, b)+(b > a) or +(b > 0))
