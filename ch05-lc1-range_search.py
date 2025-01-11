class BSTNode:
    def search_range(self, lower_bound, upper_bound):
        in_range = []
        if self.val > lower_bound:
            if self.left is not None:
                in_range.extend(self.left.search_range(lower_bound, upper_bound))
        if self.val >= lower_bound and self.val <= upper_bound:
            in_range.append(self.val)
        if self.val < upper_bound:
            if self.right is not None:
                in_range.extend(self.right.search_range(lower_bound, upper_bound))
        return in_range
