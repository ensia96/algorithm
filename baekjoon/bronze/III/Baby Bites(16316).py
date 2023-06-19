n = int(input())
x = 0
for i in input().split():
    x += x+1 == int(i)if i.isdigit()else 1
print(['something is fishy', 'makes sense'][x == n])
