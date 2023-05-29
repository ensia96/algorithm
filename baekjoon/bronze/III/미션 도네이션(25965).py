for i in range(int(input())):
    m = int(input())
    A = [[*map(int, input().split())]for _ in ' '*m]
    k, d, a = map(int, input().split())
    print(sum(max(0, x*k-y*d+z*a)for x, y, z in A))
