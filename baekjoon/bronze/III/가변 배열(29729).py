s, _, _, *A = map(int, open(0).read().split())
t = 0
for a in A:
    t += -1+2*a
    s *= 1+(t > s)
print(s)
