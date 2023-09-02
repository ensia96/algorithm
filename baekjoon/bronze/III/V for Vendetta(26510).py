x, y = ' *'
for i in map(int, input().split()):
    for j in range(i):
        print(x*j+y+x*(1+2*(i-j-2))+y*(i-j > 1))
