class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = k = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                k += 1
                i += 1
            j += 1
            
        return k
                