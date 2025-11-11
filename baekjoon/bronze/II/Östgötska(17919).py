W = input().split()
print(["dae ae ju traeligt va", "haer talar vi rikssvenska"]
      [len(W) * 4 > sum('ae' in w for w in W) * 10])
