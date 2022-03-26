while 1:
    a, b = map(int, input().split())
    if not a+b:
        break
    print(('neither'if a % b else'multiple')if b % a else'factor')
