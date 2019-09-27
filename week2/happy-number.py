class Solution:
    def isHappy(self, n: int) -> bool:
        if (n == 1):
            return True
        else:
            result = set()
            while (n != 1):
                n = sum([int(i) ** 2 for i in str(n)])
                if n in result:
                    return False
                else:
                    result.add(n)
            return True