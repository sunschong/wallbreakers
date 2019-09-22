class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [x for x in s.lower() if x.isalnum()]
        rev = list(cleaned)
        rev.reverse()
        return cleaned == rev