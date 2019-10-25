from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
            
        s = [i for i in sorted(d, key=d.get, reverse=True)]
        return s[:k]