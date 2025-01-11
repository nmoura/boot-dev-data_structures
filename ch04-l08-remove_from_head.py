from node import Node


class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        temp_head_node = self.head
        self.head = temp_head_node.next
        if self.head is None:
            self.tail = None
        return temp_head_node

    # don't touch below this line

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)

