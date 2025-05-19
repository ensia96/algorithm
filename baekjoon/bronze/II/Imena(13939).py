input()
for s in input().split('.')[:-1]:
    print(sum(not (sum(i.isdigit()for i in i))
          and i[0].isupper()for i in s.split()))
