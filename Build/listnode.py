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
