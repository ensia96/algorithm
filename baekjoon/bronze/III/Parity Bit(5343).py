for _ in ' '*int(input()):
    l = input()
    print(sum(l[8*i:8*i+7].count('1') != int(l[8*i+7])
          for i in range(len(l)//8)))
