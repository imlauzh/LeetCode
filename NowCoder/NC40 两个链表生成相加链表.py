# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
# 栈
class Solution:
    def buildList(self, nums):
        self.head = ListNode(nums[-1])
        curr = self.head
        for i in range(len(nums)-2, -1, -1):
            curr.next = ListNode(nums[i])
            curr = curr.next

    def addInList(self, head1, head2):
        # write code here
        # 链表转移到栈
        stack1, stack2 = [], []
        while head1 or head2:
            if head1:
                stack1.append(head1.val)
                head1 = head1.next
            if head2:
                stack2.append(head2.val)
                head2 = head2.next
        carry, nums = 0, []
        # 同时pop计算进位，记录余数
        while stack1 and stack2:
            a, b = stack1.pop(), stack2.pop()
            calc = (a+b+carry) % 10
            carry = (a+b+carry)//10
            nums.append(calc)
        # 把剩下的也计算上
        stack1 += stack2
        while stack1 or carry == 1:
            if stack1:
                a = stack1.pop()
            else:
                a = 0
            calc = (a+carry) % 10
            carry = (a+carry)//10
            nums.append(calc)
        # 数组转换成链表并返回
        self.buildList(nums)
        return self.head


# 链表翻转
class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        prev.next = None
        while curr:
            nxt = curr.next
            curr.next, prev, curr = prev, curr, nxt
        return prev

    def addInList(self, head1, head2):
        # write code here
        # 首先翻转两个链表
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)
        head, carry = head1, 0
        # 计算都有的位置
        while head1 and head2:
            sumVal = head1.val+head2.val+carry
            head1.val = sumVal % 10
            carry = sumVal//10
            # 记录tail，便于衔接剩下的链表长度
            tail = head1
            head1, head2 = head1.next, head2.next
        # 链表2是长的
        if head2:
            # tail接上链表2
            tail.next = head2
            while carry > 0 and head2:
                sumVal = head2.val+carry
                head2.val = sumVal % 10
                carry = sumVal//10
                # 更新tail
                tail = head2
                head2 = head2.next
        # 链表1是长的
        elif head1:
            while carry > 0 and head1:
                sumVal = head1.val+carry
                head1.val = sumVal % 10
                carry = sumVal//10
                tail = head1
                head1 = head1.next
        # 如果都计算完了还有进位，则在tail后面加上
        if carry > 0:
            carry = ListNode(carry)
            tail.next = carry
        # 返回翻转的链表
        return self.reverse(head)
