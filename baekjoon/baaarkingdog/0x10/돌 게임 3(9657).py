n = int(input())
D = [0, 1, 0, 1, 1]
for i in range(5, n+1):
    D += [not D[i-1]*D[i-3]*D[i-4]]
print(['CY', 'SK'][D[n]])
