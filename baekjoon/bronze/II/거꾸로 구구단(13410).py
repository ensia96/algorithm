n, m = map(int, input().split())
print(max(int(str(n*-~i)[::-1])for i in range(m)))
