for _ in ' ' * int(input()):
    print(*[y for y in map(int, input().split(','))if y %
          4 < 1 or y % 400 < 1 and y % 100])
