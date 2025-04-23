while (l := input()) != '0 0':
    n, m = map(int, l.split())
    print(max(map(sum, zip(*[map(int, input().split())for _ in ' '*m]))))
