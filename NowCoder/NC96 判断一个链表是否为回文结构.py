# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self, head):
        # write code here
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        return nodes == nodes[::-1]
