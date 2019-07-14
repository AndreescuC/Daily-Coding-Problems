from solve import Node, serialize, deserialize


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    print('Success')


if __name__ == '__main__':
    main()
