# reference to @StefanPochmann answer, there are three solutions, they are very concise and efficient,  very worthed learning.
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
# The second solution is recursive, a little slowly than the first.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cop1 = cop2 = head
        i = 0
        for _ in range(n):
            cop1 = cop1.next
        if not cop1:
            return head.next
        while cop1.next:
            cop1 = cop1.next
            cop2 = cop2.next
        cop2.next = cop2.next.next  
        return head
 
class Solution:
    def removeNthFromEnd(self, head, n):

        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i + 1, (head, head.next)[i + 1 == n]
        return remove(head)[1]
