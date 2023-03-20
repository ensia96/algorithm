for _ in ' '*int(input()):
    A = [i for i in map(int, input().split())if not i % 2]
    print(sum(A), min(A))
