A = [eval(l.replace(*' /'))for l in [*open(0)][1:]]
print(min(A), max(A), sum(A))
