l, _ = lambda: map(int, input().split()), 0
n, k = l()
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = l()
    for j in range(k+1):
        d[i][j] = d[i-1][j]
        if j >= w:
            d[i][j] = max(v+d[i-1][j-w], d[i][j])

print(d[n][k])

# d[i][j] = i번째 물건을 선택하는 시점에 중량이 j일때의 최대 가치
# 점화식 : d[i][j] = max(d[i+1][j], v + d[i+1][j-w] if j>= w)
# 도움 받은 글 : https://www.acmicpc.net/board/view/46105
# 영상 참고 : https://www.youtube.com/watch?v=wFP5VHGHFdk
