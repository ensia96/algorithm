a = b = c = i = j = k = 0
for _ in ' '*int(input()):
    x, y, z = map(int, input().split())
    a, b, c = x+max(a, b), y+max(a, b, c), z+max(b, c)
    i, j, k = x+min(i, j), y+min(i, j, k), z+min(j, k)
print(max(a, b, c), min(i, j, k))
