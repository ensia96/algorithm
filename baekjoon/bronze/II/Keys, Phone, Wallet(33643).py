_, *A = open(0)
print(*[i for i in ["keys", "phone", "wallet"]if i + '\n'not in A] or ['ready'])
