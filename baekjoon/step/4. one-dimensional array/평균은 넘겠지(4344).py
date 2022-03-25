a = int(input())
for i in range(a):
    a, *b = map(int, input().split())
    c = sum(b) / a
    print("{:.3f}%".format(len(list(filter(lambda x: x > c, b))) / a * 100))
