for _ in '   ':
    x = sum(int(input())for _ in ' '*int(input()))
    print('0+-'[(x > 0)+2*(x < 0)])
