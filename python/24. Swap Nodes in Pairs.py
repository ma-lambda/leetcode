class Solution(object):
    def swapPairs(self, head):
    if not head or not head.next: return head
        result = cur = ListNode(0)
        num = 1
        while head:
            if num % 2 == 1:
                tmp = ListNode(head.val)
            else:
                cur.next = ListNode(head.val)
                cur = cur.next
                cur.next = tmp
                cur = cur.next
            head = head.next
            num += 1
        if num % 2 == 0:
            cur.next = tmp
        return result.next
