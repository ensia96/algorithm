d = [0, 1, 2, 4]
for _ in range(int(input())):
    n, c = int(input()), len(d)-1
    _ = [0, [d.append(sum(d[i-2:i+1]) % (10**9+9))for i in range(c, n)]][c < n]
    print(d[n])
