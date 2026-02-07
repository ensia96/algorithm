r, c = map(int, input().split())
print(r * (~-r)**~-c % 998244353)
