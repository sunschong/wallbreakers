class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # add 1 to last element
        digits[-1] += 1
            
        for i in range(len(digits) - 1, 0, -1):
            if(digits[i] != 10):
                break
            digits[i] = 0
            digits[i-1] += 1
            
        if digits[0] != 10:
            return digits
        else:
            digits[0] = 0
            return [1] + digits