a = input()
a = [i % 2 for i in map(a.count, a)]
print(2*any(a)-all(a))
