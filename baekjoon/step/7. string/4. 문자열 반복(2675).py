for _ in range(int(input())):
    i, s = input().split()
    i = int(i)
    print("".join([j * i for j in s]))
