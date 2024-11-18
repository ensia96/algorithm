A, a, B, b, P = map(int, input().split())
print("YNeos"[1 - (A + B <= P or a >= B or b >= A) :: 2])
