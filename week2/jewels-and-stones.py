class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = set(J)
        count  = 0
        for x in S:
            if x in j:
                count += 1
                
        return count