class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        result = []
        for x in st:
            result.append(x[::-1])
        return ' '.join(result)