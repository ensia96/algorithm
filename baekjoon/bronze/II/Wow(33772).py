x = '\\../'
print([*open(0)][1].replace(x * 2, 'w').replace(x, 'v')[::2])
