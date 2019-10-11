class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        start = 0
        end = len(nums) - 1
        while start <= mid and end >= mid:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            mid = (end + start) // 2
        return -1