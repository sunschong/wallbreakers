class Solution:
    def titleToNumber(self, s: str) -> int:
        #A-Z = 1-26
        #AA-AZ = 27 - 52
        result = 0
        for x in s:
            result = result * 26 + ord(x) - 64 #uppercase starts at 65 for A
        return result