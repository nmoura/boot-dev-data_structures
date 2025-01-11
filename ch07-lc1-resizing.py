class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
        if self.current_load() >= 0.05:
            new_hashmap = HashMap(len(self.hashmap) * 10)
            for item in self.hashmap:
                if isinstance(item, tuple):
                    new_hashmap.insert(item[0], item[1])
            self.hashmap = new_hashmap.hashmap

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        filled_buckets = len(self.hashmap) - self.hashmap.count(None)
        return filled_buckets / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

