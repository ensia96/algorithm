input()
l = 0
for i in input():
    print(l ^ (l := int(i)), end='')
