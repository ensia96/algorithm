f, n = lambda x: x < 2 or x*f(x-1), 2.5
print("n e\n- -----------\n0 1\n1 2\n2 2.5")
for i in range(3, 10):
    n += 1/f(i)
    print(i, f"{n:.9f}")
