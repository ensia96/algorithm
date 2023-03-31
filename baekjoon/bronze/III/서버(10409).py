_, t = map(int, input().split())
for i, j in enumerate(map(int, input().split())):
    t -= j
    t < 0 and exit(print(i))
print(i+1)
