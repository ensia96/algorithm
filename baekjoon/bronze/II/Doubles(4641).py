while (l := input().split())[1:]:
    print(sum(str(int(x) * 2) in l for x in l) - 1)
