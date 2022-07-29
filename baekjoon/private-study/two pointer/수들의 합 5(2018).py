n = int(input())
c = l = r = S = 1
while l*2 <= n:
    if S >= n:
        c += S == n
        l = r = S = l+1
    r += 1
    S += r
print(c)
