class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        for out_idx in range(len(document)):
            level = self.root
            for inn_idx in range(out_idx, len(document)):
                if document[inn_idx] in variations.keys():
                    char = variations[document[inn_idx]]
                else:
                    char = document[inn_idx]
                if char not in level:
                    break
                else:
                    level = level[char]
                if self.end_symbol in level:
                    matches.add(document[out_idx:inn_idx + 1])
        return matches


    # don't touch below this line

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

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

