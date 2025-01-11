class Trie:
    def add(self, word):
        current = self.root
        for c in word:
            try:
                current[c]
            except KeyError:
                current[c] = {}
            current = current[c]
        current[self.end_symbol] = True

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

