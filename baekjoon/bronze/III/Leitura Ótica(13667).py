while 1:
    n = int(input())
    if not n:
        break
    for i in range(n):
        T = [a < 128 for a in map(int, input().split())]
        print('*'if 1 < T.count(1)else 'ABCDE'[T.index(1)])
