n, k = map(int, input().split())
m = int(5e5)
l = [[0, 0] for _ in range(m + 1)]
d, r, c = [n], -1, 0

while 1:
    q, x = d, k + (c*(1+c)//2)
    d = []
    if x > m:
        exit(print(-1))
    for p in q:
        i = (c+1) % 2
        if p == x or l[x][c % 2]:
            exit(print(c))
        for a in [p-1, p+1, p*2]:
            if 0 <= a <= m and not l[a][i]:
                d += [a]
                l[a][i] = 1
    c += 1

# 풀이 참고 : https://ijsilver.tistory.com/30
