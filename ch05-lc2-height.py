class BSTNode:
    def height(self):
        left_subtree, right_subtree = 0, 0
        if self.val is None:
            return 0
        if self.left is not None:
            left_subtree = self.left.height()
        if self.right is not None:
            right_subtree = self.right.height()
        return max(left_subtree, right_subtree) + 1
