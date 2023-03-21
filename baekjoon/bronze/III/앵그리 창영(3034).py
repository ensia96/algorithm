n, w, h = map(int, input().split())
x = (w*w+h*h)**.5
for _ in ' '*n:
    print('DNAE'[int(input()) > x::2])
