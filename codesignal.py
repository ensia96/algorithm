def longestWord(text):
    from string import ascii_letters

    words = "".join([_ if _ in list(ascii_letters) else " " for _ in text]).split(" ")
    return max(words, key=len)


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def longestWord(text):
    return max(re.split("[^a-zA-Z]", text), key=len)


# def longestWord(t):
#     return max(
#         "".join([i if i in string.ascii_letters else " " for i in t]).split(), key=len
#     )


# ================================================#
#                 question v                     #
# ================================================#

# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

# Example

# For text = "Ready, steady, go!", the output should be
# longestWord(text) = "steady".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string text

# Guaranteed constraints:
# 4 ≤ text.length ≤ 50.

# [output] string

# The longest word from text. It's guaranteed that there is a unique output.
