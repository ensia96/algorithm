import sys
i, l, p = sys.stdin.readline, [0]*(10**4+1), 0
k = n = int(i())
_ = [exec('l[int(i())]+=1') for _ in ' '*n]
for w in range(10**4+1):
    if l[w]:
        p = max(p, w*k)
        k -= l[w]
print(p)
