class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_set = set(t)
        i = j = 0
        k = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                k += 1
            j += 1
        return k == len(s)