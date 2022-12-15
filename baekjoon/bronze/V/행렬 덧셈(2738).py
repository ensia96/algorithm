l, f = lambda: [*map(int, input().split())
                ], lambda x: print(*map(sum, zip(*x)))
n, _ = l()
[*map(lambda x:print(*map(sum, zip(*x))), zip(*eval('[l()for _ in" "*n],'*2)))]
