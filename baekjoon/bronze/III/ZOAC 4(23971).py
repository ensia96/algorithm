h, w, n, m = map(int, input().split())
print(sum(divmod(h, n+1))*sum(divmod(w, m+1)))
