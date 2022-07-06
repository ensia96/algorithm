x, y = map(int, input().split())
z, l, r, a = int(y*100 / x)+1, 0, 10**9, -1
while l <= r:
    m = (l+r)//2
    if int((y+m)*100 / (x+m)) >= z:
        r, a = m-1, m
    else:
        l = m+1
print(a)
