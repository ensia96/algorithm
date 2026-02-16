for i in range(int(input())):
    _, A, B, C, D = eval('[*map(int,input().split())],' * 5)
    print('Case #%d:' % -~i, sum(a ^ b ^ c ^ d ==
          _[1]for a in A for b in B for c in C for d in D))
