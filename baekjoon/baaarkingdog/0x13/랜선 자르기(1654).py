k, n = map(int, input().split())
K = [int(input())for _ in ' '*k]
s, e = 1, 2**31-1
while s < e:
    m = (s+e+1)//2
    if sum(map(lambda x: x//m, K)) >= n: s = m
    else:
        e = m-1
print(s)
