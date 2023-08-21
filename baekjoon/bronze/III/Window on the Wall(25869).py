a, b, c = map(int, input().split())
print(max(0, a-c-c)*max(0, b-c-c))
