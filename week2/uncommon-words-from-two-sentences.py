from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        s1 = A.split()
        s2 = B.split()
        d = defaultdict(int)
        result = []
        
        for w in s1:
            d[w] += 1
        for w in s2:
            d[w] += 1
        return [w for w, i in d.items() if i == 1]