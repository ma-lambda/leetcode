# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or not head:
            return head
        result = cur = ListNode(0)
        num = 1
        tmp = []
        while head:
            tmp.append(ListNode(head.val))
            if num % k == 0:
                for node in tmp[::-1]:
                    cur.next = node
                    cur = cur.next
                tmp = []
            num += 1
            head = head.next
        if tmp:
            for node in tmp:
                cur.next = node
                cur = cur.next
        return result.next
