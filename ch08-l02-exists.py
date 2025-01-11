class Trie:
    def exists(self, word):
        current = self.root
        for letter in word:
            try:
                current[letter]
            except KeyError:
                return False
            current = current[letter]
        if current == { self.end_symbol: True }:
            return True
        return False

    # don't touch below this line

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

