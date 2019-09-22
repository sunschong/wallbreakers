class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left, right + 1):
            n = i 
            while(n > 0):
                d = n % 10
                if(d == 0 or i % d != 0):
                    break
                n = n // 10
            if (n == 0):
                nums.append(i)
                
        return nums