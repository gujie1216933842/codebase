old_list = [
    {'age': 10, 'name': 'tom15'},
    {'age': 14, 'name': 'tom14'},
    {'age': 12, 'name': 'tom12'},
]

'''
需求:根据age键排序

'''
# new_dict = {}
# for k,v in enumerate(old_list):
#     new_dict[v['age']] = v
#
# print(new_dict.items())
# d = sorted(new_dict.items(), key = lambda k: k[0])
# print(d)


a = sorted(old_list, key=lambda k: k['name'])
print(a)
