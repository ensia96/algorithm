while (l := input()) >= '1':
    n, k = map(int, l.split())
    s = 1
    b = k
    exec(
        "v,r=input().split();v=int(v);s=max(s,v*(r>'R'));b=min(b,[k,v][r<'C']);" * n)
    print(s + 1, b - 1)
