n = int(input())
D = [0]*(n+1)
for i in map(int, input().split()):
    D[i] = D[i-1]+1
print(n-max(D))
