class Trie:
    def find_matches(self, document):
        matches = set()
        for out_idx in range(len(document)):
            level = self.root
            for inn_idx in range(out_idx, len(document)):
                if document[inn_idx] not in level:
                    break
                else:
                    level = level[document[inn_idx]]
                if self.end_symbol in level:
                    matches.add(document[out_idx:inn_idx + 1])
        return matches


    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

