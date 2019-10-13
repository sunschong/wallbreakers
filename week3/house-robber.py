from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        # step >= 2 < len(nums)
        def helper(nums, n, memo):
            if n < 0:
                return 0
            if memo[n] >= 0:
                return memo[n]
            
            a = max(nums[n] + helper(nums, n - 2, memo), helper(nums, n - 1, memo))
            memo[n] = a
            return a
            
        memo = defaultdict(lambda: -1)
        return helper(nums, len(nums) - 1, memo)
    