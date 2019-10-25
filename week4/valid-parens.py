class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {']':'[','}':'{', ')':'('}
        
        for x in s:
            if x in d.values():
                stack.append(x)
            elif x in d.keys():
                if not stack:
                    return False
                elif stack.pop() != d[x]:
                    return False
        
        return len(stack) == 0