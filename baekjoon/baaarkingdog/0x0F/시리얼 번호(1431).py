print('\n'.join(sorted([input() for _ in range(int(input()))], key=lambda x: (
    len(x), sum(int(c) for c in x if c.isdigit()), x))))
