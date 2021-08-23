a = [0 for _ in range(26)]
b = [*a]

for s in input():
    a[ord(s) - 97] += 1
for s in input():
    b[ord(s) - 97] += 1

print(sum(abs(a[i] - b[i]) for i in range(26)))
