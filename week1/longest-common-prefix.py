class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        curr = ""
        i = 0
        j = 0
        if len(strs) == 1:
            return strs[0]
        elif len(strs) != 0:
            strlen = len(min(strs, key=len))
            while j < strlen and i < len(strs):
                curr = strs[i][j]
                while i < len(strs):
                    if strs[i][j] != curr:
                        return pre
                    i += 1
                pre += curr
                i = 0
                j += 1
        return pre