m = 10**4
p = [0, 0]+[1]*(m-1)
for i in range(2, m+1):
    if p[i]:
        p[i+i::i] = [0]*(m//i-1)

for _ in ' '*int(input()):
    a, b = map(int, input().split())
    q, v = [(a, 0)], [0]*10**4
    for n, c in q:
        if n == b:
            break
        l = [n//10*10, n-n//10 % 10*10, n-n//100 % 10*100, n % 1000]
        for i in range(4)[::-1]:
            for k in range(10):
                T = l[i]+k*10**i
                if (T > 1000)*p[T]*(not v[T]):
                    v[T] = 1
                    q += [(T, c+1)]
    else:
        c = 'Impossible'
    print(c)
