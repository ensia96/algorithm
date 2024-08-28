A = sorted(map(int, [*open(0)][1:]))[-42:]
print(sum(A), sum((59 < a) + (99 < a) + (139 < a) + (199 < a) + (249 < a) for a in A))
