n = int(input())
A = [input()for _ in ' '*n]
for _ in ' '*int(input()):
    x = int(input())
    print(f'Rule {x}:', A[x-1]if 0 < x <= n else 'No such rule')
