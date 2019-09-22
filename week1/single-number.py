class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # linear time, no extra memory
        result = 0
        for x in nums:
            result ^= x
            
        return result