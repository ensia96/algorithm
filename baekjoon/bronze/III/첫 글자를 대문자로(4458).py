for _ in ' '*int(input()):
    a, *A = input()
    x = ord(a)
    print(chr(x-(x > 90)*32)+''.join(A))
