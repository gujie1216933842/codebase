'''
构建二叉树
'''


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Traverse(object):
    def __init__(self, root):
        self.root = root

    def Is_empty(self):
        if not self.root:
            return True
        else:
            return False


    def pre(self, treeNode):
        '''前序遍历'''
        if not treeNode:
            return
        print(treeNode.value)
        self.pre(treeNode.left)
        self.pre(treeNode.right)

    def mid(self, treeNode):
        '''前序遍历'''
        if not treeNode:
            return
        self.pre(treeNode.left)
        print(treeNode.value)
        self.pre(treeNode.right)

    def after(self, treeNode):
        '''前序遍历'''
        if not treeNode:
            return
        self.after(treeNode.left)
        print(treeNode.value)
        self.after(treeNode.left)


n1 = Node(value=1)
n2 = Node(2, n1, 0)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5, n3, n4)
n6 = Node(6, n2, n5)
n7 = Node(7, n6, 0)
n8 = Node(8)
root = Node('root', n7, n8)

bt = Traverse(root)
print('pre......')
print(bt.pre(bt.root))
print('mid......')
print(bt.mid(bt.root))
print('after.....')
print(bt.after(bt.root))

