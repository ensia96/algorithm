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
