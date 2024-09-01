A = input()
(*T,) = filter(str.isalpha, A)
C = len(T)
print((sum(69 - ord(t) + (t == "F") for t in T) + 0.5 * (len(A) - C)) / C)
