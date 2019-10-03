import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', ' ')
        p = paragraph.lower().split()
        bset = set(banned)
        punc = set("!?',;.")
        c = collections.Counter()
        
        for i in range(len(p)):
            word = ''
            for x in p[i]:
                if x not in punc:
                    word += x
            p[i] = word
            
        c.update(p)
        print(p)
        result, max_c = '', 0
        for w in c:
            if c[w] > max_c and w not in bset:
                result, max_c = w, c[w]
        return result
            