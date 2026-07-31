class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        n = len(s)
        m = n % k
        return "-".join([s[:m]] * (m > 0) + [s[i:i + k] for i in range(m, n, k)])
