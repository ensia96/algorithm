a, b = input().split()
a, b = sum(map(int, a))*len(a), sum(map(int, b))*len(b)
print((a > b)+2*(a < b))
