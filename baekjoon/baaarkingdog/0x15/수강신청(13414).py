k, l = map(int, input().split())
L = {input(): i for i in range(l)}
for n in sorted(L, key=lambda x: L[x])[:k]: print(n)
