# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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


root_r = TreeNode(1)
root_r.insertion(5)
root_r.insertion(3)

root_r.printPreOrder()
x = Solution()
print(x.getMinimumDifference(root_r))
print(x.inorderTraversal(root_r))