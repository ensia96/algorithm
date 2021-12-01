g, t = lambda a, b: (a == 0)*b or g(b % a, a), int(input())
for _ in ' '*t:
    m, n, x, y = map(int, input().split())
    x, y = x*(not x == m), y*(not y == n)
    for i in range(x, m//g(m, n)*n+1, m):
        if i*(i % n == y):
            print(i)
            break
    else:
        print(-1)
