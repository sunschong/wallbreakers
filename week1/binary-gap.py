class Solution:
    def binaryGap(self, N: int) -> int:
        result = 0
        prev = None 
        for i in range(32): #32bits in an int
            if (N >> i) & 1:
                if prev != None:
                    result = max(result, i - prev)
                prev = i
        return result