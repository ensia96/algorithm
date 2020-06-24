def evenDigitsOnly(n):
    for i in str(n):
        if int(i) % 2 == 1:
            return False
    return True

#================================================#
#     ^ my answer      ||  most voted answer v   #
#================================================#

def evenDigitsOnly(n):
    return all([int(i)%2==0 for i in str(n)])

#================================================#
#                 question v                     #
#================================================#

# Check if all digits of the given integer are even.

# Example

# For n = 248622, the output should be
# evenDigitsOnly(n) = true;
# For n = 642386, the output should be
# evenDigitsOnly(n) = false.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 1 ≤ n ≤ 109.

# [output] boolean

# true if all digits of n are even, false otherwise.