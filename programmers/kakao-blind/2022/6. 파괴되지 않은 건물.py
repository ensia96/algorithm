def solution(board, skill):
    R = range
    n, m = len(board), len(board[0])
    C = [[0]*-~m for _ in ' '*-~n]

    for t, a, b, c, d, e in skill:
        f = (2*(t-1)-1)*e
        C[a][b] += f
        C[a][d+1] -= f
        C[c+1][b] -= f
        C[c+1][d+1] += f

    for i in R(1, n+1):
        for j in R(m+1):
            C[i][j] += C[i-1][j]
    for i in R(n+1):
        for j in R(1, m+1):
            C[i][j] += C[i][j-1]

    return sum(board[i][j]+C[i][j] > 0 for i in R(n)for j in R(m))

# 신입 공채 당시에 제출했던 코드
#
# # 정확성 통과, 효율성 0
#
# def action(t, a, b, c, d, e, m):
#     n = e*(-1 if t == 1 else 1)
#     for i in range(a, c+1):
#         for j in range(b, d+1):
#             m[i][j] += n
#     return m
#
#
# def solution(board, skill):
#     answer = sum(map(sum, board))
#     for act in skill:
#         board = action(*act, board)
#     return sum(len([*filter(lambda x: x > 0, line)]) for line in board)
