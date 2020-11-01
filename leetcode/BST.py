# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  # used for # 116, not used in BST

    def insertion(self, val):
        nodeR = self
        new_node = TreeNode(val)
        while nodeR:
            if val < nodeR.val:
                if nodeR.left:
                    nodeR = nodeR.left
                else:
                    nodeR.left = new_node
            elif val > nodeR.val:
                if nodeR.right:
                    nodeR = nodeR.right
                else:
                    nodeR.right = new_node
            else:
                return

    def printPreOrder(self):
        if self is None:
            return
        print(self.val, end=", ")
        if self.left:
            self.left.printPreOrder()
        if self.right:
            self.right.printPreOrder()


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 530 BST, find minimum difference
        import sys

        def inOrder(node):
            nonlocal res, pre
            if node is None:
                return
            inOrder(node.left)
            if pre != -1:
                res = min(res, node.val - pre)
            pre = node.val
            inOrder(node.right)

        pre = -1
        res = sys.maxsize
        inOrder(root)
        return res

    def inorderTraversal(self, root: TreeNode):
        # 94 typical recursive solution
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res

    def connect(self, root):
        # 116 Populating Next Right Pointers in Each Node
        # given a perfect binary tree
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:  # when at level N, link the nodes at level N+1
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

    def postOrderTwoStack(self, root: TreeNode):
        if root is None:
            return
        stack = [root]
        ans = []
        while len(stack) != 0:
            tmp = stack.pop()
            ans.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        ans.reverse()

        return ans

    def postOrderOneStack(self, root: TreeNode):
        i = 1
        stack = []
        while len(stack) != 0 or i == 1:
            while root is not None:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
                i = 2 * i
            item = stack.pop()
            root = item

            if item.right and len(stack) != 0:
                if item.right == stack[-1]:
                    temp = stack.pop()
                    stack.append(root)
                    root = temp
                else:
                    print(root.val, end=' ')
                    root = None
            else:
                print(root.val, end=' ')
                root = None


root_r = TreeNode(15)
root_r.insertion(8)
root_r.insertion(0)
root_r.insertion(4)
root_r.insertion(-1)
root_r.insertion(1)
root_r.insertion(3)
root_r.insertion(5)


root_r.insertion(17)
root_r.insertion(16)
root_r.insertion(19)


x = Solution()
x.postOrderOneStack(root_r)
print(x.postOrderTwoStack(root_r))
