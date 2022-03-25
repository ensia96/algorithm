for i in range(int(input())):
    x = 0
    for j in map(len, input().split("X")):
        while j:
            x += j
            j -= 1
    print(x)
