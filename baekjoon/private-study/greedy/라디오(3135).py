a, b = map(int, input().split())
A = [int(input())for _ in ' '*int(input())]
print(min(abs(a-b), min(abs(a-b)for a in A)+1))
