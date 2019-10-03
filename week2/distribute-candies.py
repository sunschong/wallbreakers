class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        #max number of candies is half of list
        #kinds of candies = set(candies)
        m = len(candies) // 2
        kinds = len(set(candies))
        return min(m, kinds)
