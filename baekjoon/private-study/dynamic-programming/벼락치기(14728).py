n, t = map(int, input().split())
D = -~t*[0]
for _ in ' '*n:
    k, s = map(int, input().split())
    D = k > t and D or [max(D[j], (D[j-k]+s)*(j >= k))for j in range(t+1)]
print(D[-1])
