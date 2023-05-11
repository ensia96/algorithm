n, a = map(int, open(0).read().split())
if n > 5:
    print("Love is open door")
else:
    for i in range(n-1):
        a = -~-a
        print(a)
