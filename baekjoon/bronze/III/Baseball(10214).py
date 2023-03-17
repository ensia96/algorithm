for _ in ' '*int(input()):
    x = y = 0
    exec('a,b=map(int,input().split());x+=a;y+=b;'*9)
    print(['YKoonrseeai'[x < y::2], 'Draw'][x == y])
