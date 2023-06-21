for i in range(int(input())):
    a, b = map(int, input().split())
    x, y = divmod(a, b)
    print(f'Case {i+1}:', *[x]if x else [], *[f'{y}/{b}']if y else [])
