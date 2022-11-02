i = 1
while 1:
    A = [*input()]
    if '-' in A:
        exit()
    S, a = [], 0
    while A:
        x = A.pop()
        if x == '}':
            S += x,
        elif S:
            S.pop()
        else:
            S += '}'
            a += 1
    print(f"{i}. {a+len(S)//2}")
    i += 1
