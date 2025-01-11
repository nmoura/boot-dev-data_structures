from stack import Stack


OPENING_PARENTHESIS = '('


def is_balanced(input_str):
    parenthesis_stack = Stack()
    
    for char in input_str:
        if char == OPENING_PARENTHESIS:
            parenthesis_stack.push(char)
        elif not parenthesis_stack.pop():
            return False

    if parenthesis_stack.size() > 0:
        return False
        
    return True

a = '()'
b = '()()'
c = '((()))'
d = '(()(()))'
print(is_balanced(a))
print(is_balanced(b))
print(is_balanced(c))
print(is_balanced(d))

z = '('
y = '())'
x = '(()()'
w = '(()))'
print(is_balanced(z))
print(is_balanced(y))
print(is_balanced(x))
print(is_balanced(w))
