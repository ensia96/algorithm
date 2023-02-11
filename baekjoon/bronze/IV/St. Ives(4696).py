while 1:
    a = float(input())
    if not a:
        break
    print(f'{1+a+a*a+a**3+a**4:.2f}')
