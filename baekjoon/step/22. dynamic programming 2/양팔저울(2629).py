n = int(input())
W = [*map(int, input().split())]+[0]
D = [[0]*15001 for _ in ' '*31]


def f(i, w):
    if i > n or D[i][w]:
        return
    D[i][w] = 1
    f(i+1, w+W[i])
    f(i+1, abs(w-W[i]))
    f(i+1, w)


f(0, 0)
input()
print(*['N'if i > 15000 or not D[n][i]else'Y'for i in map(int, input().split())])
