import collections as c
n = int(input())
b = sorted([int(input()) for _ in range(n)])
a = c.Counter(b).most_common()

print(round(sum(b)/n))
print(b[len(b)//2])
print(a[1][0] if len(a) > 1 and a[0][1] == a[1][1] else a[0][0])
print(max(b)-min(b))

# 숏코딩에서 statistics 모듈 사용한 코드를 봄
# from statistics import*
# n,*l=map(int,open(0))
# print('%.0f'%mean(l),median(l),sorted(multimode(l))[:2][-1],max(l)-min(l))
