l, c = lambda: map(int, input().split()), 0
n, m = l()
l = [*map(str, sorted(l()))]
s, v, d = [0] * m, [0] * n, {}


def b(c):
    if c == m:
        t = ' '.join(s)
        if t not in d:
            d[t] = 0
        return
    for i in range(n):
        if not v[i]:
            s[c], v[i] = l[i], 1
            b(c+1)
            v[i] = 0


b(c)
print('\n'.join(d))

# 딕셔너리(해시 테이블) 자료형에 대한 아이디어를 얻은 글 : https://jinho-study.tistory.com/1042
