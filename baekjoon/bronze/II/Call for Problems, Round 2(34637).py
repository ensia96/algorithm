h, *a = open(0)
print(min(int(h.split()[1]), len({*map(int, a)})))
