h, m = map(int, input().split(':'))
t = (h*60+m)*59
print(f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}")
