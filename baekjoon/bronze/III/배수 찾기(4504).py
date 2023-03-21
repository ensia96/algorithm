x, y = int(input()), int(input())
while y:
    print(f'{y} is {"NOT "*(not y%x)}a multiple of {x}.')
    y = int(input())
