n = int(input())
D = [0, 1, 1, 1]
for i in range(4, n+1):
    D += [not D[i-1] or not D[i-3]]
print(['CY', 'SK'][D[n]])
