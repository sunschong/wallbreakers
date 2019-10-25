class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for s in S:
            if s == '#':
                if len(stack1) > 0:
                    stack1.pop()
            else:
                stack1.append(s)
        
        for t in T: 
            if t == '#':
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(t)
                
        
        return ''.join(stack1) == ''.join(stack2)