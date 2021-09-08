import sys
i, r, f = sys.stdin.readline, range, {}
l, n, b = lambda: map(int, i().split()), int(i()), 301
for _ in r(n):
    m, d, M, D = l()
    s, e = m*100+d, M*100+D
    f[s] = max(f.get(s, 0), e)
i = m = a = 0
t = sorted(f)
while b <= 1130:
    for k in r(i, len(t)):
        if t[k] > b:
            break
        if f[t[k]] > m:
            m, i = f[t[k]], k
    if m == b:
        exit(print(0))
    b, a = m, a+1
print(a)

# 풀이 참고 : https://j3sung.tistory.com/508
