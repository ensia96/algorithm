_, m = map(int, input().split())
x = 1
for i in map(int, input().split()):
    x = x*i % m
print(x)
