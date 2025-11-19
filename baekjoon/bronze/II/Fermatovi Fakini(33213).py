I = input
n = int(I())
A = {*map(int, I().split())}
t = [2, 1][sum(a % 2 for a in A) * 2 > n]
while t in A:
    t += 2
print(t)
