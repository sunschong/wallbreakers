# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
     
        for i in range(len(lists)):
            curr = lists[i]
            while curr != None:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        if len(heap) == 0:
            return
        head = ListNode(heapq.heappop(heap))
        curr = head
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
            
        return head