t = 0
a, b = input().split()
print(*[[b, a][(t := t + 1) % 2] for a, b in zip(a, b)], sep="")
