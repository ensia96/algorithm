while n := int(input()):
    print(max(eval('input(),' * n), key=lambda a: sum(a.count(c * 2)
          for c in 'aeiouy')))
