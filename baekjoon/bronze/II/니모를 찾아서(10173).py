while 1:
    s = input()
    if s == "EOI":
        break
    print('nemo' in s.lower() and 'Found' or 'Missing')
