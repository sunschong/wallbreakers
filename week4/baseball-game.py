class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for x in ops:
            if x == 'C':
                stack.pop()
            elif x == 'D':
                stack.append(2 * stack[-1])
            elif x == '+':
                num = stack[-1] + stack[-2]
                stack.append(num)
            else:
                stack.append(int(x))
                
        return sum(stack)