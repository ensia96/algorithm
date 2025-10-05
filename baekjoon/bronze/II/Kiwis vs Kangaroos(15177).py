t = sum("kangaroo".count(i) - "kiwibird".count(i)for i in input().lower())
print(["Feud continues", "Kiwis", "Kangaroos"][(t < 0) + 2 * (t > 0)])
