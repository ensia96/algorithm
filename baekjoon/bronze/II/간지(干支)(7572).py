n = (int(input())-4) % 60
print(f"{chr(65+n%12)}{n%10}")
