class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split(' ')
        if (len(s) != len(pattern)):
            return False
        return len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s))