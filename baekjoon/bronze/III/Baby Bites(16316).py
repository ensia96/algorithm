n = int(input())
x = 0
for i in input().split():
    x += [1, x+1 == int(i)][i.isdigit()]
print(['something is fishy', 'makes sense'][x == n])
