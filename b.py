
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2018-04-25 22:30:06
# @Last Modified by:   anchen
# @Last Modified time: 2018-04-25 23:03:15



'''
二分查找法
'''
def binarySearch(l, t):
    low, high = 0, len(l) - 1
    while low < high:           
        mid = int((low + high) / 2)
        if l[mid] > t:
            high = mid
        elif l[mid] < t:
            low = mid + 1
        else:
            return mid
    return low if l[low] == t else False
 
if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    # print (binarySearch(l, 12) )
    # print (binarySearch(l, 1) )
    # print (binarySearch(l, 13) )
    # print (binarySearch(l, 444) )



def select_index(l,item):
    low = 0
    high = len(l)-1
    while low < high:
        half = int((low + high)/2)
        print(half)
        if l[half] < item:
           low = half  
        elif l[half] > item:
           high = half -1
        else:
           return half
           

l = [1, 4, 12, 45, 66, 99, 120, 444]
print(select_index(l, 12) )















