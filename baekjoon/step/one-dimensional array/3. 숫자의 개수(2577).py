a = [0] * 10
for s in str(int(input()) * int(input()) * int(input())):
    a[int(s)] += 1
for i in a:
    print(i)
