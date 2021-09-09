n = int(input())
w = [int(input()) for _ in range(n)]
if n < 3:
    exit(print(sum(w)))
d = [(w[0], 0), (w[1], w[0]+w[1])]
_ = [d.append((max(d[i-2])+w[i], d[i-1][0]+w[i]))for i in range(2, n)]
print(max(max(i) for i in d))
