n, *A = map(int, open(0).read().split())
print(max(-(n//-2)-A.count(1), 0))
