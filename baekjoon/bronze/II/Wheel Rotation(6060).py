_, *T = map(int, open(0).read().split()[3::3])
for t in T:
    _ ^= t
print(_)
