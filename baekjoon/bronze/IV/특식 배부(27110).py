n = int(input())
print(sum(map(lambda x: min(int(x), n), input().split())))
