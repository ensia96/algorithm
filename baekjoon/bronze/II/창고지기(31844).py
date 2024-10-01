A = input()
x, y, z = map(A.find, "!@#")
print([0, x - y, y - x][(x > z > y) + 2 * (x < z < y)] - 1)
