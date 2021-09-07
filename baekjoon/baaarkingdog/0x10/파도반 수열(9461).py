d = [0, 1, 1, 1, 2, 2, 3, 4]
for _ in range(int(input())):
    n, c = int(input()), len(d)-1
    _ = [0, [d.append(d[i-4]+d[i]) for i in range(c, n)]][c < n]
    print(d[n])
