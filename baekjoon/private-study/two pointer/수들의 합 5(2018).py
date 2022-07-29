n = int(input())
c = l = r = 1
S = 0
while l <= r <= n:
    if S < n:
        S += r
        r += 1
    else:
        c += S == n
        S -= l
        l += 1
print(c)
