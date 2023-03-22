for _ in ' '*int(input()):
    c, v = eval('divmod('+input().replace(*' ,')+')')
    print(f'You get {c} piece(s) and your dad gets {v} piece(s).')
