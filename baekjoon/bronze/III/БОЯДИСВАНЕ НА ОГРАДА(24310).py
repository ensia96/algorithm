a, b, c, d = map(int, input().split())
a, b = sorted((a, b))
c, d = sorted((c, d))
print([[max(a, b, c, d)-min(a, b, c, d)+1, max(b-a, d-c)+1]
      [(a < c and d < b) or (c < a and b < d)], b-a+d-c+2][b < c or d < a])
