class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u', 'A', 'E','I','O','U'}
        copy = list(s)
        j = len(s) - 1
        i = 0
        while (i < j):
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                copy[i], copy[j] = s[j], s[i]
                j -= 1
                i += 1
        return ''.join(copy)