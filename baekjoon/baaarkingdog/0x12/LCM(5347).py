g, t = lambda a, b: (a == 0)*b or g(b % a, a), int(input())
for _ in ' '*t:
    a, b = map(int, input().split())
    print(a*b//g(a, b))
