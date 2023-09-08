while 1:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        T = [a < 128 for a in map(int, input().split())]
        print('*'if 1 != T.count(True)else 'ABCDE'[T.index(True)])
