t, x, y, z = 0, 1, 31, 96
input()
for i in input():
    t += (ord(i)-z)*x
    x *= y
print(t)
