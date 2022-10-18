input()
c = 0
for i in map(int, input().split()):
    c += (i == c % 3)
print(c)
