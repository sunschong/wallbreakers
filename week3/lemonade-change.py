from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = defaultdict(int)
        for m in bills:
            if m == 10:
                if wallet[5] == 0:
                    return False
                else:
                    wallet[5] -= 1
            elif m == 20:
                if wallet[10] >= 0 and wallet[5] == 0:
                    return False
                elif wallet[5] < 3 and wallet[10] == 0:
                    return False
                elif wallet[10] >= 1 and wallet[5] >= 1:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
            wallet[m] += 1
        return True