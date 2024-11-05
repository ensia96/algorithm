l, *A = open(0)
n, x = l.split()
print(sum((x in a.split()[0].split("_")) * int(a.split()[1]) for a in A))
