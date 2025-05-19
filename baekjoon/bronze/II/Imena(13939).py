input()
for s in input().split('.')[:-1]:
    print(sum(i[0].isupper() and all(map(str.islower, i[1:]))
          for i in s.split()))
