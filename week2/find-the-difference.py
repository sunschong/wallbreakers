import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        for l in tc:
            if sc[l] != tc[l]:
                return l