# This is my first answer which is too slow to face "time limit error", though it really work.
class Solution(object):
    def mergeKLists(self, lists):
        cur = ListNode(0)
        result = cur
        lists = [node for node in lists if node]
        if len(lists) == 0:
            return result.next
        if len(lists) == 1:
            return lists[0]
        while True:
            minvalue = lists[0].val
            index = 0
            for i in range(len(lists)):
                if lists[i].val < minvalue:
                    minvalue = lists[i].val
                    index = i
            cur.next = lists[index]
            lists[index] = lists[index].next
            if not lists[index]:
                del lists[index]
            cur = cur.next
            if len(lists) == 1:
                cur.next = lists[0]
                return result.next

# This my second solution which using the function sorted(), cost 193ms
class Solution(object):
    def mergeKLists(self, lists):
        cur = ListNode(0)
        result = cur
        lists = [node for node in lists if node]
        if len(lists) == 0:
            return result.next
        if len(lists) == 1:
            return lists[0]
        lists = sorted(lists, key = lambda x: x.val)
        while True:
            if lists[0].val > lists[1].val: # if False, it means the first value of all nodes is sorted
                lists = sorted(lists, key = lambda x: x.val)
            cur.next = lists[0]
            cur = cur.next
            lists[0] = lists[0].next
            if not lists[0]:
                del lists[0]
            if len(lists) == 1:
                cur.next = lists[0]
                return result.next
            if len(lists) == 0:
                return result.next

# This a solution using priority queue by @Fibo, but I didn't test, because it can't found queue
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        k = len(lists)
        q = PriorityQueue(maxsize=k)
        dummy = ListNode(None)
        curr = dummy
        for list_idx, node in enumerate(lists):
            if node: q.put((node.val, list_idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, list_idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, list_idx, curr.next))
        return dummy.next
