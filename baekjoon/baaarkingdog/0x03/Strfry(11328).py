for _ in range(int(input())):
    a, b = input().split()
    print(f"{'P' if sorted(a) == sorted(b) else 'Imp'}ossible")
