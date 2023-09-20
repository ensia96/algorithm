D = {'d': ' qb', 'b': ' pd', 'p': ' bq', 'q': ' dp'}
a, b = map(int, input().split())
for _ in ' '*a:
    print(''.join(D[i][b]for i in input()))
