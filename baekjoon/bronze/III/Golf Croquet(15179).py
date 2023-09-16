a, b, c, d = open(0)
a, b = a.strip(), b.strip()
t, *T = [0]*3
for i in d:
    T[t] += (i in 'HD')+(6 > T[t] and 'D' == i)
    T[not t] += i == 'O'
    t = not t
    if max(T) > 6:
        break
x, y = T
z = [' is winning', ' has won'][max(T) > 6]
print(a, x, b, f"{y}.", ["All square", a+z, b+z][(x > y)+2*(x < y)]+'.')
