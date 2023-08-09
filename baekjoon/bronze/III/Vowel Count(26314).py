for _ in ' '*int(input()):
    A = input()
    print(A)
    print(+(len(A) < sum(map(A.count, "aeiou"))*2))
