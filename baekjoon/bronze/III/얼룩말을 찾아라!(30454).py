import re
_, _, *A = open(0).read().split()
T = [0]*501
for a in A:
    T[re.sub(r"(.)\1+", r"\1", a).count('1')] += 1
t = max(T)
print(T.index(t), t)
