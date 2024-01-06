_, m, d = map(int, input().split('-'))
x = m*100+d
print('Capricorn'if x < 120 else 'Aquarius'if x < 219 else 'Pisces'if x < 321 else 'Aries'if x < 420 else 'Taurus'if x < 521 else 'Gemini'if x < 621 else 'Cancer'if x <
      723 else 'Leo'if x < 823 else 'Virgo'if x < 923 else 'Libra'if x < 1023 else 'Scorpio'if x < 1123 else 'Sagittarius'if x < 1222 else 'Capricorn')
