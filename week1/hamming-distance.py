class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #num bits that are different between x and y
        return bin(x^y).count('1')