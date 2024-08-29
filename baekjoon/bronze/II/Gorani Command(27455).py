def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    r = 1
    c = 1
    N = 50
    M = 50

    index = 2

    # Finding the minimum in the first column
    for i in range(1, n):
        x = int(data[index])
        index += 1
        if x < N:
            r = i
            N = x

    x = int(data[index])
    index += 1
    if x < N:
        r = n
    M = x

    # Finding the minimum in the first row
    for i in range(2, m + 1):
        x = int(data[index])
        index += 1
        if x < M:
            c = i
            M = x

    print(r, c)


if __name__ == "__main__":
    main()
