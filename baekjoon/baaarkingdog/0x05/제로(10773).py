s = []

for _ in range(int(input())):
    n = int(input())
    if n:
        s.append(n)
    else:
        if s:
            s.pop()

print(sum(s))
