n = int(input())
D = [1, 0, 1, 0, 1, 1]
for i in range(6, n+1):
    D += not D[i-1] or not D[i-3] or not D[i-4],
print(['CY', 'SK'][D[n]])
