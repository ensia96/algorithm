A = input()
T = [0] * 5
x = "0128"
for a in A:
    T[x.find(a)] += 1
a, b, c, d, e = T
print(x[(not e) and 1 + bool(a * b * c * d) + (a == b == c == d)])
