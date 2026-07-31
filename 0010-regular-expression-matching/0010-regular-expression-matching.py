class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.match(s, p, 0, 0)

    def match(self, s, p, i, j):
        if j == len(p):
            return i == len(s)

        firstMatch = False
        if i < len(s) and (p[j] == s[i] or p[j] == '.'):
            firstMatch = True

        if j + 1 < len(p) and p[j + 1] == '*':
            skip = self.match(s, p, i, j + 2)
            useIt = firstMatch and self.match(s, p, i + 1, j)
            return skip or useIt
        else:
            return firstMatch and self.match(s, p, i + 1, j + 1)