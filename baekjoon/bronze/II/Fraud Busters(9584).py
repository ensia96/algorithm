l, _, *A = open(0)
T = [a[:-1] for a in A if sum(l[i] == "*" or a[i] == l[i] for i in range(9)) == 9]
print(len(T))
[*map(print, T)]
