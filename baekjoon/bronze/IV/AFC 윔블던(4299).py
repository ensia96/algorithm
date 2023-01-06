a, b = map(int, input().split())
x = (a+b)//2
y = a-x
print(*[[max(x, y), min(x, y)], [-1]][x < 0 or y < 0 or x-y != b])
