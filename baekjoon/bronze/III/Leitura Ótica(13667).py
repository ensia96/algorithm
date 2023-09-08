while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        T = [a < 128 for a in map(int, input().split())]
        print('*' if T.count(True) != 1 else 'ABCDE'[T.index(True)])
