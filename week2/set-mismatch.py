import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        n1, n2 = 0, 0
        for n in range(1, len(nums) + 1):
            if c[n] > 1:
                n1 = n
            if c[n] == 0:
                n2 = n
        return [n1, n2]