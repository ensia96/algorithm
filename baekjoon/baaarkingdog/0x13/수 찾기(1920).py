n = int(input())
A = sorted(map(int, input().split()))
_ = input()
for b in map(int, input().split()):
    s, e, f = 0, n-1, 0
    while s <= e:
        m = (s+e)//2
        if A[m] == b:
            f = 1
            break
        elif A[m] > b:
            e = m-1
        else:
            s = m+1
    print(f)
