class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = next


class SingleLinkList(object):
    '''单链表'''

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        pass

    def length(self):
        '''链表长度'''
        pass

    def travel(self):
        '''链表遍历'''



        pass

    def add(self, item):
        '''链表头部添加元素'''
        pass

    def append(self, item):
        '''链表尾部添加元素'''
        pass

    def insert(self, pos, item):
        '''链表指定位置添加元素'''
        pass

    def remove(self, item):
        '''删除节点'''
        pass

    def search(self, item):
        '''查找节点是否存在'''
        pass


'''测试'''
if __name__ == "__main__":
    sll = SingleLinkList()
