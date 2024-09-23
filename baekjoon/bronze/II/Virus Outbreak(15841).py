F = [0, 1]
for i in range(500):
    F += (F[-1] + F[-2],)
for i in [*map(int, open(0))][:-1]:
    print(f"Hour {i}: {F[i]} cow(s) affected")
