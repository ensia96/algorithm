import re
_, _, *A = open(0).read().split()
T = {}
for a in A:
    t = re.sub(r"(.)\1+", r"\1", a).count('1')
    T[t] = T.get(t, 0)+1
t = max(T)
print(t, T[t])
