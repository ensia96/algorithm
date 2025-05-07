_, A, B = open(0)
print(*sorted(set(map(int, A.split())).intersection(set(map(int, B.split())))))
