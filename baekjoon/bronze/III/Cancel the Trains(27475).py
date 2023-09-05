I, L = input, lambda: map(int, input().split())
for _ in ' '*int(I()):
    input()
    print(len({*L()} & {*L()}))
