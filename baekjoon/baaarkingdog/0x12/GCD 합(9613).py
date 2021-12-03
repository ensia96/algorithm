g, r = lambda a, b: (a == 0)*b or g(b % a, a), range
for _ in ' '*int(input()):
    n, *L = map(int, input().split())
    print(sum(g(L[i], L[j])for i in r(n)for j in r(i+1, n)))
