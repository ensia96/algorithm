a = 1
while a:
    a, b = map(int, input().split())
    a and print(('neither'if a % b else'multiple')if b % a else'factor')
