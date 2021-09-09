n = int(input())
w = [int(input()) for _ in range(n)]
if n <= 2:
    exit(print(sum(w)))
d = [(w[0], 0), (w[1], w[0]+w[1])]+[0]*(n-2)
for i in range(2, n):
    d[i] = (max(d[i-2])+w[i], d[i-1][0]+w[i])
print(max(max(i) for i in d))
