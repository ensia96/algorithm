def alphabeticShift(inputString):
    from string import ascii_letters
    spells = list(ascii_letters)
    return ''.join([spells[spells.index(spell)+1].lower() for spell in list(inputString)])
#================================================#
#     ^ my answer      ||  most voted answer v   #
#================================================#

def alphabeticShift(s):
    return "".join(chr((ord(i)-96)%26+97) for i in s)

#================================================#
#                 question v                     #
#================================================#

# Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

# Example

# For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# A non-empty string consisting of lowercase English characters.

# Guaranteed constraints:
# 1 ≤ inputString.length ≤ 1000.

# [output] string

# The resulting string after repl