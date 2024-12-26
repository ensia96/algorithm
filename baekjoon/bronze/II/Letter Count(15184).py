A = input().upper()
for i in map(chr, range(65, 91)):
    print(i, "|", "*" * A.count(i))
