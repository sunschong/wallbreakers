class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr1 = headA
        curr2 = headB
        s = set()
        while curr1 != None:
            s.add(curr1)
            curr1 = curr1.next
        
        while curr2 != None:
            if curr2 in s:
                return curr2
            curr2 = curr2.next
        