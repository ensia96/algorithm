n = []
_ = [n.append(l.split()) for l in [*open(0)]]
print(*sorted(map(int, [i[::-1] for i in n[1:]])))
