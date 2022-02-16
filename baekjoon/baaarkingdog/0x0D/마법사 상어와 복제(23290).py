from sys import stdin
from collections import deque

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

input = stdin.readline

m, s = map(int, input().split())
fish_board = [[[[], []] for _ in range(4)] for _ in range(4)]
smell_board = [[0]*4 for _ in range(4)]
for _ in range(m):
    x, y, d = map(int, input().split())
    fish_board[x-1][y-1][0].append(d-1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1
path = []
max_fish_count = -1

visited = [[False]*4 for _ in range(4)]


def solv():
    global path, max_fish_count
    for now in range(s):
        start_copy_fish()

        move_target = move_fish()
        renew_fish_board(move_target)

        path = []
        max_fish_count = -1

        select_move_shark_path(sx, sy, 0, 0, [])
        move_shark()

        reduce_smell()

        end_copy_fish()
    answer = 0
    for x in range(4):
        for y in range(4):
            answer += len(fish_board[x][y][0])
    print(answer)


def reduce_smell():
    global smell_board
    for x in range(4):
        for y in range(4):
            if smell_board[x][y] > 0:
                smell_board[x][y] -= 1


def move_shark():
    global sx, sy, fish_board, smell_board
    for d in path:
        sx += sdx[d]
        sy += sdy[d]
        if fish_board[sx][sy][0]:
            fish_board[sx][sy][0] = []
            smell_board[sx][sy] = 3


def select_move_shark_path(x, y, fish_count, move_count, tmp_path):
    global sx, sy, visited, max_fish_count, path
    if move_count == 3:
        if max_fish_count < fish_count:
            max_fish_count = fish_count
            path = [d for d in tmp_path]
        return
    for d in range(4):
        nx = x + sdx[d]
        ny = y + sdy[d]
        if boundary_validator(nx, ny):
            if not visited[nx][ny]:
                visited[nx][ny] = True
                nxt_fish_count = fish_count + len(fish_board[nx][ny][0])
                select_move_shark_path(
                    nx, ny, nxt_fish_count, move_count+1, tmp_path+[d])
                visited[nx][ny] = False
            else:
                select_move_shark_path(
                    nx, ny, fish_count, move_count+1, tmp_path+[d])


def renew_fish_board(move_target):
    global fish_board
    for x, y, nd in move_target:
        fish_board[x][y][0].append(nd)


def move_fish():
    move_target = []
    for x in range(4):
        for y in range(4):
            while fish_board[x][y][0]:
                nd = fish_board[x][y][0].pop()
                flag = False
                for _ in range(8):
                    nx = x + dx[nd]
                    ny = y + dy[nd]
                    if point_validator(nx, ny):
                        move_target.append((nx, ny, nd))
                        flag = True
                        break
                    nd = (nd - 1) % 8
                if not flag:
                    move_target.append((x, y, nd))
    return move_target


def boundary_validator(x, y):
    if x < 0 or y < 0 or x >= 4 or y >= 4:
        return False
    return True


def point_validator(x, y):
    if not boundary_validator(x, y):
        return False
    elif smell_board[x][y] != 0:
        return False
    elif (x, y) == (sx, sy):
        return False
    return True


def start_copy_fish():
    for x in range(4):
        for y in range(4):
            for d in fish_board[x][y][0]:
                fish_board[x][y][1].append(d)


def end_copy_fish():
    global fish_board
    for x in range(4):
        for y in range(4):
            while fish_board[x][y][1]:
                fish_board[x][y][0].append(fish_board[x][y][1].pop())


solv()

# 내 풀이 -> 예제 통과 못함.. -> 원인을 모르겠음
#
# L, F = lambda: map(int, input().split()), [0]*16
# m, s = L()
# C = [(*L(),)for _ in ' '*m]
# S = (*L(),)
# g, T = lambda x, y: 0 < x <= 4 and 0 < y <= 4, [0]*16
# for x, y, d in C:
#     F[x*4+y-5] += 1
# Z = [(i, j, k)for i in range(4)for j in range(4)for k in range(4)]
#
#
# def f():
#     t = []
#     for x, y, d in C:
#         D = [(x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1),
#              (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1)]
#         for h in range(8):
#             z = (d-h) % 8
#             i, j = D[z-1]
#             if g(i, j) and not T[i*4+j-5] and (i, j) != S:
#                 F[x*4+y-5] -= 1
#                 F[i*4+j-5] += 1
#                 t += (i, j, z),
#                 break
#         else:
#             t += (x, y, d),
#     return t
#
#
# for _ in ' '*s:
#     t = C[::]
#     C = f()
#     E = {}
#     for z in Z:
#         i, j, s, Q = *S, 0, []
#         for d in z:
#             i, j = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)][d]
#             if not g(i, j):
#                 break
#             s += F[i*4+j-5]*((i, j) not in Q)
#             Q += (i, j),
#         else:
#             E[s] = E.get(s) or Q
#     Q = E[max(E)]
#     for i, j in Q:
#         x = i*4+j-5
#         T[x] = F[x] and 3
#         F[x] = 0
#     S = Q[-1]
#     C = [(i, j, d)for i, j, d in C if F[i*4+j-5]]
#     T = [t and t-1 for t in T]
#     for i, j, z in t:
#         F[i*4+j-5] += 1
#     C += t
# print(sum(F))
