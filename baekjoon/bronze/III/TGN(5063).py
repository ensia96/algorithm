for _ in ' '*int(input()):
    r, e, c = map(int, input().split())
    print('do not advertise'if r > e -
          c else 'advertise'if r < e-c else 'does not matter')
