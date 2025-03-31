while A := sum(map(int, input().split())):
    print(
        *[[i, chr((ord(i) - 98 - (A % 25)) % 26 + 97)][i.isalpha()] for i in input()],
        sep="",
    )
