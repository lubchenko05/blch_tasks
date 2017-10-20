import random
"""
Напишіть функцію, щоб перевірити, чи є двійкове дерево дійсним двійковим деревом пошуку.
"""


class BinaryTreeNode:
    def __init__(self, v):
        self.v = v
        self.__left = None
        self.__right = None

    def insert_left(self, left_value):
        self.__left = BinaryTreeNode(left_value)
        return self.__left

    def insert_right(self, right_value):
        self.__right = BinaryTreeNode(right_value)
        return self.__right

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def __str__(self):
        return str(self.v)


def generate_tree():
    choices = range(1, 10)
    tree = BinaryTreeNode(random.choice(choices))
    tree_left = tree.insert_left(random.choice(choices))
    tree_right = tree.insert_right(random.choice(choices))
    tree_left_left = tree_left.insert_left(random.choice(choices))
    tree_left_right = tree_left.insert_right(random.choice(choices))
    tree_right_left = tree_right.insert_left(random.choice(choices))
    tree_right_right = tree_right.insert_right(random.choice(choices))
    tree_left_left_left = tree_left_left.insert_left(random.choice(choices))
    tree_left_left_right = tree_left_left.insert_right(random.choice(choices))
    tree_right_left_left = tree_right_left.insert_left(random.choice(choices))
    tree_right_left_right = tree_right_left.insert_right(random.choice(choices))
    levels = [' '*24+str(tree.v),
              ' ' * 8 + str(tree_left.v) + ' ' * 32 + str(tree_right.v),
              ' ' * 2 + str(tree_left_left.v) + ' ' * 12 + str(tree_left_right.v) + ' ' * 19 + str(
                  tree_right_left.v) + ' ' * 12 + str(tree_right_right.v),
              str(tree_left_left_left.v) + ' ' * 3 + str(tree_left_left_right.v)+' '*28+str(
                  tree_right_left_left.v)+' '*3 + str(tree_right_left_right.v)
              ]

    return tree, '\n\n'.join(levels)


def check_tree(root: BinaryTreeNode):

    def _check(root: BinaryTreeNode, flag=None):
        flag = False
        if root.get_left():
            flag = _check(root.get_left())
            if flag:
                return root, flag
        if root.get_right():
            flag = _check(root.get_right())
            if flag:
                return root, flag
        if root.get_left() and root.get_right():
            if root.get_left().v > root.get_right().v:
                flag = True
        return flag

    return not _check(root)


if __name__ == "__main__":
    for i in range(100):
        tree, str_tree = generate_tree()
        result = check_tree(tree)
        if result:
            print('\n'*2)
            print(str_tree)
            print(result)
