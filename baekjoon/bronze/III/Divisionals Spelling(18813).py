_, m, *L = open(0).read().split()
m = int(m)
T = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(sum(all(l.count(t) < 1+(t in T[:m])for t in T)for l in L))
