# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLinked(head: ListNode):
    if head is None:
        return
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

    def hasCycle(self, head: ListNode) -> bool:
        # 141 linked list cycle detect
        # no additional memory needed, Floyd’s Cycle-Finding Algorithm
        if head is None or head.next is None:
            return False
        fast = slow = head
        while fast and slow:
            if fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        # 142 move one pointer, n^2 time complexity, O(1) space complexity
        def distance(ln1: ListNode, ln2: ListNode) -> int:
            dis = 0
            while ln1 is not ln2:
                dis = dis + 1
                ln1 = ln1.next
            return dis

        fast = head
        curr_dis = 0
        prev_dis = -1
        while prev_dis < curr_dis and fast is not None:
            prev_dis = curr_dis
            fast = fast.next
            curr_dis = distance(head, fast)

        if fast is None:
            return None
        return fast
        while curr_dis > 0:
            head = head.next
            curr_dis = curr_dis - 1
        return head

    def detectCycle2(self, head: ListNode) -> ListNode:
        # 142 double pointer, slow and fast
        # O(n) time complexity; O(1) space complexity
        if head is None or head.next is None:
            return None
        fast = slow = head
        while fast and slow:
            if fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while head is not slow:
                    head = head.next
                    slow = slow.next
                return head
        return None

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 82 remove duplicates from sorted list, only distinct values kept
        if head is None:
            return head

        first_node = prev = link = head
        head = head.next
        val = head.val
        same2 = False
        store = head.next.val
        while head is not None:
            if store is head.val:
                head = head.next
                same2 = True
                continue
            elif head.next is not None:
                if head.next.val is head.val:
                    same2 = True
                    store = head.val
                    head = head.next
                    continue
            same2 = False
            prev.next = head
            prev = head
            head = head.next
            if head.next is not None:
                store = head.next.val

        if head is None and same2 is True:
            prev.next = None
        if first_node is None:
            return None

        elif first_node.val is val:
            if first_node.next.val is val:
                return first_node.next.next
            return first_node.next
        else:
            return first_node

    def swapPairs(self, head: ListNode) -> ListNode:
        # 24 swap every two adjacency pairs, iterative
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp = dummyHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummyHead.next

    def swapPairs2(self, head: ListNode) -> ListNode:
        # 14 recursive
        def rec_swap(node):
            if not node:
                return None
            elif not node.next:
                return node

            to_link = rec_swap(node.next.next)
            node2 = node.next
            node.next = to_link
            node2.next = node
            return node2

        return rec_swap(head)


last = first = ListNode(1, None)
for i in range(2, 3):
    first = ListNode(i, first)


# printLinked(first)
x = Solution()
# new = x.removeNthRec(first, 9)
printLinked(first)
# print(x.hasCycle(first))
res = x.swapPairs(first)
printLinked(res)
