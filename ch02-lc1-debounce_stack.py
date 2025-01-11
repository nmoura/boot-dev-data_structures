from stack import Stack


class DebounceStack(Stack):
    def push(self, item):
        if super().peek() != item:
            super().push(item)


ds = DebounceStack()
actions = ["like_post", "like_post", "unlike_post", "unlike_post", "like_post"]

for action in actions:
    ds.push(action)

result = []

while ds.size() != 0:
    result.insert(0, ds.pop())

print(result)
