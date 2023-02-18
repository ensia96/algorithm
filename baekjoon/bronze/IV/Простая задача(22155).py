for _ in ' '*int(input()):
    i, f = map(int, input().split())
    print('YNeos'[bool((i*f > 2)+(i > 2)+(f > 2))::2])
