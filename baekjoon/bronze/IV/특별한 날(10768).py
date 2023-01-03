a, b = int(input()), int(input())
if 2 < a or 2 == a and 18 < b:
    print('After')
elif (a, b) == (2, 18):
    print('Special')
else:
    print('Before')
