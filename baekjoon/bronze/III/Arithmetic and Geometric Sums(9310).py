n = int(input())
while n:
    a, b, c = map(int, input().split())
    print([a*((b//a)**n-1)//(b//a-1), n*(2*a+(n-1)*(b-a))//2][c-b == b-a])
    n = int(input())
