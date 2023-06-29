I, _ = lambda: map(int, input().split()), 0
x, y = I()
while x+y:
    print(sum(min(i, y//x)for i in I()))
    x, y = I()
