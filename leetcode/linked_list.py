class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLinked(head: ListNode):
    while head.next:
        print(head.val, end=", ")
        head = head.next
    print(head.val)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 19 Remove the Nth node from the end and return the list's head
        # two pointer, fast/slow
        ptr0 = ptr1 = head
        count = 0
        while count < n and ptr1.next:
            ptr1 = ptr1.next
            count = count + 1

        if count == n - 1:  # delete the nth element, only n elements in the list
            return ptr0.next

        while ptr1.next:
            ptr1 = ptr1.next
            ptr0 = ptr0.next

        temp = ptr0.next
        if temp:
            temp1 = temp.next
            ptr0.next = temp1
        else:
            ptr0.next = None

        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # 19 a bit modify, not guarantee a better performance
        ptr0 = ptr1 = head
        while n > 0:
            ptr1 = ptr1.next
            n = n - 1

        if ptr1 is None:
            return head.next

        while ptr1.next:
            ptr1 = ptr1.next
            ptr0 = ptr0.next

        if ptr0.next:
            ptr0.next = ptr0.next.next
        else:
            ptr0.next = None

        return head

    def removeNthRec(self, head: ListNode, n: int) -> ListNode:
        # 19 a recursive solution
        def recFind(node):
            if node is None:
                return 0
            count = recFind(node.next)

            if count is n:
                if node.next.next is not None:
                    node.next = node.next.next
                else:
                    node.next = None
            return count + 1

        result = recFind(head)
        if result is n:
            return head.next
        return head


first = ListNode(1, None)
for i in range(2, 10):
    first = ListNode(i, first)
printLinked(first)
x = Solution()
new = x.removeNthRec(first, 9)
printLinked(new)
