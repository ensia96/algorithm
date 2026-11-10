class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        return len({(i := e.split('@'))[0].split('+')[0].replace('.', '') + '@' + i[1] for e in emails})
