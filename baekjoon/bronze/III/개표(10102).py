input()
x = 'AB'
a, b = map(input().count, x)
print([x[a < b], 'Tie'][a == b])
