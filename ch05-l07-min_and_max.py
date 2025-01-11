class BSTNode:
    def get_min(self):
        if self.left is None:
            return self.val
        min = self.left
        while min.left is not None:
            min = min.left
        return min.val

    def get_max(self):
        if self.right is None:
            return self.val
        min = self.right
        while min.right is not None:
            min = min.right
        return min.val

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

