_, a, b = open(0)
print(sum(a == b == "C" for a, b in zip(a, b)))
