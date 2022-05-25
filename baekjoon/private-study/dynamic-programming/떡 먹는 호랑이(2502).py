d, k = map(int, input().split())
a, b = 0, 1
for i in range(d-2):
    a, b = b, a+b
for i in range(1, k):
    t = k-i*a
    t % b or exit(print(f"{i}\n{t//b}"))
