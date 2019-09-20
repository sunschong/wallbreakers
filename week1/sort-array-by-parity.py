class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # have 2 arrays to store odd and even separately
        odd = []
        even = []
        for n in A:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        return even + odd