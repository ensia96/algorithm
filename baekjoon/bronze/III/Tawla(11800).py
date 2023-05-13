A = ["Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]
B = ["HabbYakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]
for i in range(int(input())):
    a, b = sorted(map(int, input().split()))
    print(f'Case {i+1}:', [[f"{A[b-1]} {A[a-1]}", B[a-1]]
          [a == b], "Sheesh Beesh"][a+b == 11])
