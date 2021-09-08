a, *b = [sum(map(int, s.split('+')))for s in input().split('-')]
print(a-sum(b))
