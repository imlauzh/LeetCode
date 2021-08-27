# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self , head ):
        # write code here
        # 需要用一个头发结点
        # 因为头节点可能和下一个结点相等
        res=ListNode(0)
        res.next=head
        prev=res
        curr=head
        while curr and curr.next:
            # 当前和下一个不等
            # 因为是有序链表，所以可以认为curr只出现一次
            if curr.val!=curr.next.val:
                prev=curr
                curr=curr.next
            else:
                # 否则的话需要一次遍历，直到下一个不等
                # 把这中间的结点删除（跳过）
                while curr.val==curr.next.val:
                    curr=curr.next
                    if not curr.next:
                        break
                prev.next=curr.next
                curr=curr.next
        return res.next
