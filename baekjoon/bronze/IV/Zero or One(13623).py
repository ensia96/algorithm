a, b, c = map(int, input().split())
print('*ABC'[((b == c)+2*(c == a)+3*(a == b)) % 6])
