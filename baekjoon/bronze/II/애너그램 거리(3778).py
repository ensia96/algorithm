S = "abcdefghijklmnopqrstuvwxyz"
for i in range(int(input())):
    print(
        f"Case #{i+1}:",
        sum(abs(i - j) for i, j in zip(map(input().count, S), map(input().count, S))),
    )
