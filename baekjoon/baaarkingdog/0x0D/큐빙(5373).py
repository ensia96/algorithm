for _ in range(int(input())):
    _, c = input(), [[_]*9 for _ in 'wyrogb']
    for i, j in input().split():
        u, d, f, b, l, r = c
        t, x, y, z, w = [(u, l, f, r, b), (d, b, r, f, l), (f, u, l, d, r),
                         (b, r, d, l, u), (l, f, u, b, d), (r, d, b, u, f)]['UDFBLR'.find(i)]
        for _ in range([3, 1][j == '+']):
            t[2], t[5], t[8], t[7], t[6], t[3], t[0], t[1] = \
                t[0], t[1], t[2], t[5], t[8], t[7], t[6], t[3]
            x[8], x[7], x[6], y[6], y[3], y[0], z[2], z[5], z[8], w[0], w[1], w[2] = \
                y[6], y[3], y[0], z[2], z[5], z[8], w[0], w[1], w[2], x[8], x[7], x[6]
    for p in c[0]:
        print(''.join(p))

# 풀이 참고 : https://conak-diary.tistory.com/99
