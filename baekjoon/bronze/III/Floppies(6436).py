x, y = 1860000, 1
while y:
    i = int(input())
    if not i:
        break
    i = i//2+i % 2
    i += i//2
    print(f'File #{y}\nJohn needs {(i+x-1)//x} floppies.\n')
    y += 1
