a, b = map(int, input().split())
x, y = map(int, input().split())
i, j = map(int, input().split())
n, m = abs(i-x)+abs(j-y), max(abs(i-a), abs(j-b))
print(['tie', 'bessie', 'daisy'][(n > m)+2*(n < m)])
