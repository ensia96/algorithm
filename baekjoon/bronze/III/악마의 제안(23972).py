k, n = map(int, input().split())
print(-(n*k//(1-n))if n != 1 else -1)
