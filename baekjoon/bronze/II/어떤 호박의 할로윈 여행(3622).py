A, a, B, b, P = map(int, input().split())
print("YNeos"[1 - (A + B <= P or (P >= A and a >= B) or (P >= B and b >= A)) :: 2])
