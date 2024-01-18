t, x, y, z, M = 0, 1, 31, 96, 1234567891
input()
for i in input():
    t = (t+(ord(i)-z)*x) % M
    x *= y
print(t)
