d, a = lambda: map(int, input().split()), 0
n, m, l = d()
r = sorted([0, *d(), l])
b = d = l
while a <= b:
    c, k = (a+b)//2, 0
    for i in range(1, len(r)):
        k += (r[i]-r[i-1]-1)//c
    if k > m:
        a = c + 1
    else:
        d = min(d, c)
        b = c-1
print(d)

# 도움 받은 글 : https://www.acmicpc.net/board/view/35663
