# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类 the head node
# @return ListNode类
#
class Solution:
    def sortInList(self, head):
        # write code here
        def getMid(head, tail):
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            return slow

        def merge(l1, l2):
            head = ListNode(0)
            curr = head
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return head.next

        def sortFuc(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            mid = getMid(head, tail)
            return merge(sortFuc(head, mid), sortFuc(mid, tail))
        return sortFuc(head, None)
