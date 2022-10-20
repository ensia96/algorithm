n, l = map(int, input().split())
A = sorted(map(int, input().split()))[::-1]
while A and l < A.pop():
    l += 1
print(l)
