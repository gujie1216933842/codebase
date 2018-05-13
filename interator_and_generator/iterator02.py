'''
创建迭代器对象
'''


class ListIterable(object):
    def __init__(self, data):
        self.__data = data

    def __iter__(self):
        print("call iterable __iter__()")
        return ListIterator(self.__data)


class ListIterator(object):
    def __init__(self, data):
        self.__data = data
        self.__count = 0

    def __iter__(self):
        print("call iterator __iter__()")
        return self

    def __next__(self):
        print("call iterator __next__()")
        if self.__count < len(self.__data):
            val = self.__data[self.__count]
            self.__count += 1
            return val
        else:
            raise StopIteration


a = ListIterable([1,2,3])
print(a)
print(type(a))