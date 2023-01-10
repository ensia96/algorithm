while 1:
    a, b, c = input().split()
    b, c = int(b), int(c)
    if not b:
        break
    print(a, 'JSue'[b > 17 or c > 79::2]+'nior')
