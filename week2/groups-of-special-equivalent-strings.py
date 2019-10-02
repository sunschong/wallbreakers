from collections import defaultdict
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        d = defaultdict(int)
        for x in A:
            #2 even indices swap if equal
            even = ''.join(sorted(x[0::2]))
            odd = ''.join(sorted(x[1::2]))
        
            d[(even, odd)] += 1
            
        return len(d)