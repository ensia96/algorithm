def messageFromBinaryCode(code):
    import binascii

    def int2bytes(i):
        hex_string = "%x" % i
        n = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

    def text_from_bits(bits, encoding="utf-8", errors="surrogatepass"):
        n = int(bits, 2)
        return int2bytes(n).decode(encoding, errors)

    return text_from_bits(code)


# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
# 파이썬에서 다양한 문자열 확인


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def messageFromBinaryCode(code):
    return "".join(
        [chr(int(code[8 * i : 8 * i + 8], 2)) for i in range(len(code) // 8)]
    )


# def messageFromBinaryCode(c):
#     return "".join([chr(int(c[i : i + 8], 2)) for i in range(0, len(c), 8)])


# ================================================#
#                 question v                     #
# ================================================#

# You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

# Assuming that your hunch is correct, decode the message.

# Example

# For code = "010010000110010101101100011011000110111100100001", the output should be
# messageFromBinaryCode(code) = "Hello!".

# The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
# Other letters can be obtained in the same manner.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string code

# A string, the encrypted message consisting of characters '0' and '1'.

# Guaranteed constraints:
# 0 < code.length < 800.

# [output] string

# The decrypted message.
