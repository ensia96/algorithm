n = int(input())
A = sorted(map(int, input().split()[:n]))
s = sum(A)
print((max((s-a)*-~-((s-a) % 2)for a in A)if s % 2 else s)//2)
