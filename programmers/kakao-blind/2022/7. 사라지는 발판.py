# 신입 공채 당시에 제출했던 코드
#
# def simulate(f, aloc, bloc, n, m, board, count):
#     if not sum(map(sum, board)):
#         return count
#     result = []
#     a, b = aloc if f else bloc
#     for y, x in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
#         if 0 <= y < n and 0 <= x < m and board[y][x]:
#             board[a][b] = 0
#     if f:
#         result += [simulate(not f, (y, x), bloc, n, m, board, count+1)]
#     else:
#         result += [simulate(not f, aloc, (y, x), n, m, board, count+1)]
#     board[a][b] = 1
#     return min(result) if result else count
#
#
# def solution(board, aloc, bloc):
#     n, m = len(board), len(board[0])
#     result = simulate(1, aloc, bloc, n, m, board, 0)
#     return result
