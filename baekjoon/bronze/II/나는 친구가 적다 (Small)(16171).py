a, b = open(0)
print(+(b[:-1] in ''.join(filter(str.isalpha, a))))
