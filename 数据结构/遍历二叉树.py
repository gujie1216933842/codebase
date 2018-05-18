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


    def pre(self,treeNode):
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
