D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for l in [*open(0)][1:]:
    print(sum(D[d]*l.count(d)for d in D.keys()))
