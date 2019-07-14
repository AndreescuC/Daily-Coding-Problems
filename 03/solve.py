class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    assert isinstance(node, Node)
    return apply_serialization(node)


def apply_serialization(node):
    if node is None:
        return '[]'

    return '[' +\
           'v:' + node.val.__repr__()[1:-1] +\
           ' l:' + apply_serialization(node.left) +\
           ' r:' + apply_serialization(node.right) +\
           ']'


def deserialize(s):
    if s == '[]':
        return None

    value = s[3:s.find(' ')]
    left, right = split_branches(s[s.find('l:'):-1])

    return Node(value, deserialize(left), deserialize(right))


def split_branches(s):
    parentheses = 0
    split_index = 0

    for index, char in enumerate(s):
        if char == '[':
            parentheses += 1
        if char == ']':
            parentheses -= 1

        if not parentheses and char == ' ':
            split_index = index
            break

    return s[s.find(":") + 1:split_index], s[split_index + len(' r:'):]
