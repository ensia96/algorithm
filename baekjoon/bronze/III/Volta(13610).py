x, y = map(int, input().split())
z = 1
while (y-x)*z < y:
    z += 1
print(z)
