class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        k = 0
        result = 0
        for i in range(len(b) - 1, 0, -1):
            bit = 1 - int(b[i])
            if bit == 1:
                result += int(math.pow(2,k))
            k += 1
        return result