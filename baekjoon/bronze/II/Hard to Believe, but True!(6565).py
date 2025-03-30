for l in open(0):
    a, b = l[::-1].split("=")
    print(int(a) == sum(map(int, b.split("+"))))
