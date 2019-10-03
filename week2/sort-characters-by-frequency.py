import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        result = ''
        for s in c.most_common():
            if s[1] > 1:
                result += s[0] * s[1]
            else:
                break
                
        for s in sorted([x for x in c if c[x] == 1]):
            result += s
        return result