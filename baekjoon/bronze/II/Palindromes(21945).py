input()
print(sum((i == i[::-1])*int(i)for i in input().split()))
