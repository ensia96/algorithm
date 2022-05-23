l, n = lambda x: x < 1 or x*l(x-1), 1
while n:
    n = int(input())
    n and print(l(2*n)//(l(n)*l(n+1)))
