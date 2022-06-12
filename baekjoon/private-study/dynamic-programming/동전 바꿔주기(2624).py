t = int(input())
k = int(input())
D = [1]+[0]*t
for _ in ' '*k:
    d = [0]*-~t
    p, n = map(int, input().split())
    for i in range(t+1):
        for j in range(n+1):
            if i+p*j > t:
                break
            d[i+p*j] += D[i]
    D = d
print(D[-1])
