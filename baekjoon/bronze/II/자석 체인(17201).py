a, b = open(0)
print("YNeos"[any(map(b.count, ["11", "22"])) :: 2])
