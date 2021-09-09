n = int(input())
w = [int(input()) for _ in range(n)]
if n < 3:
    exit(print(sum(w)))
d = [0, w[0], w[0]+w[1], max(w[0]+w[1], w[1]+w[2], w[2]+w[0])]
_ = [d.append(max(d[i-3]+w[i-1]+w[i], d[i-2]+w[i], d[i-1]))
     for i in range(3, n)]
print(d[n])

# 도움 받은 글 : https://www.acmicpc.net/board/view/73217
