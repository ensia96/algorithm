def s(n, p=["***", "* *", "***"]):
    if n == 3:
        return "\n".join(p)

    c, w = list(p), len(p)

    for i in range(w):
        c[i] += p[i] * 2
        c.append(p[i])
        c[w + i] += " " * w
        c[w + i] += p[i]

    for i in range(w):
        c.append(c[i])

    return s(n // 3, c)


print(s(int(input())))

# 풀이 참고 : https://lovelyunsh.tistory.com/114
