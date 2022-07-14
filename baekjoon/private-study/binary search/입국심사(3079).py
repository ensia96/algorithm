n, m = map(int, input().split())
T = [int(input())for _ in ' '*n]
l, r = 0, m*max(T)
while l <= r:
    x = (l+r)//2
    if sum(x//t for t in T) >= m:
        r = x-1
    else:
        l = x+1
print(l)
