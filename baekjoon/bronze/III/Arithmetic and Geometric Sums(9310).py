n = int(input())
while n:
    a, b, c = map(int, input().split())
    print(n*(2*a+(n-1)*(b-a))//2 if c-b == b-a else a*((b//a)**n-1)//(b//a-1))
    n = int(input())
