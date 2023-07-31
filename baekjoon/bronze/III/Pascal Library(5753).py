while 1:
    n, d = map(int, input().split())
    if not n+d:
        break
    print(
        'yneos'[not sum(map(all, zip(*(map(int, input().split())for _ in ' '*d))))::2])
