n, c, *A = map(int, open(0).read().split())
T = [0]*-~c
for a in A:
    for t in range(1, c//a+1):
        T[t*a] |= 1
print(sum(T))
