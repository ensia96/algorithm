while 1:
    A = input()
    if A == '#':
        break
    print(sum(a in 'aeiouAEIOU'for a in A))
