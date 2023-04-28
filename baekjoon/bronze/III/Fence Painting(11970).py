a, b = map(int, input().split())
c, d = map(int, input().split())
print([b-a+d-c, max(b, d)-min(a, c)][(c < b)*(d > a)])
