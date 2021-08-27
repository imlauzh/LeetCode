# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param lists ListNode类一维数组
# @return ListNode类
#
class Solution:
    def merge2Lists(self, l1, l2):
        if not l1 or not l2:
            return l1 if l1 else l2
        head = ListNode(0)
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return head.next

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        elif l > r:
            return None
        mid = (l+r)//2
        return self.merge2Lists(self.merge(lists, l, mid), self.merge(lists, mid+1, r))

    def mergeKLists(self, lists):
        # write code here
        return self.merge(lists, 0, len(lists)-1)
