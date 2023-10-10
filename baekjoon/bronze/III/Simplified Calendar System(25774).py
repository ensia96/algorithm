d, m, y, n = map(int, input().split())
a, b, c = map(int, input().split())
print(((((c-y)*12+b-m)*30+a-d)+n) % 7)
