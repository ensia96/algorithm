for _ in ' '*int(input()):
    a, b, c = map(int, input().split())
    print(sum(-~i % -~j == -~j % -~k == -~k % -~i for i in range(a)
          for j in range(b)for k in range(c)))
