for _ in range(int(input())):
    h, w, n = map(int, input().split())
    f, r = n % h, (n // h)
    f, r = (f, r + 1) if f else (h, r)
    print(f"{f}{r:02d}")

# fstring 관련 글 : https://seorenn.tistory.com/76
