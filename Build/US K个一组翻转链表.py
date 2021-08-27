class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        nodes = []
        curr = self
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        print(nodes)


class Solution:
    def reverse(self, head, tail):
        prev = tail.next
        curr = head
        while prev != tail:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return tail, head

    def reverseK(self, head, k):
        hair = ListNode(0)
        hair.next = head
        prev = hair

        while head:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nxt = tail.next
            head, tail = self.reverse(head, tail)
            prev.next = head
            tail.next = nxt
            prev = tail
            head = nxt
        return hair.next


if __name__ == '__main__':
    inputNodes = [1, 2, 3, 4, 5]
    k = 3
    head = ListNode(inputNodes[0])
    curr = head
    for i in range(1, len(inputNodes)):
        tmp = ListNode(inputNodes[i])
        curr.next = tmp
        curr = curr.next
    head.printNode()

    s = Solution()
    reversedNode = s.reverseK(head=head, k=k)
    reversedNode.printNode()
