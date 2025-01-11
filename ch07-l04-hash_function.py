class HashMap:
    # this is a simple hash function to work as a foundation of the hashmap
    # example for learning purposes. it doesn't resize when it gets full,
    # doesn't handle collisions and doesn't distribute keys evenly
    def key_to_index(self, key):
        unicode_chars_sum = 0
        for char in key:
            unicode_chars_sum += ord(char)
        return unicode_chars_sum % len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v is not None:
                buckets.append(v)
        return str(buckets)

