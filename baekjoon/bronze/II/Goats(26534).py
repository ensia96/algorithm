A, B = input().split(), input().split()
print(f"{sum(a > b for a in A for b in B) / sum(a != b for a in A for b in B):.5f}")
