r = ["D", "C", "B", "A", "E"]

print("\n".join([r[sum(map(int, l.split()))] for l in [*open(0)]]))
