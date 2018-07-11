'''
在Python中，
    json.dumps()    将dict转换成str
    json.loads()    将str转换成dict

'''

import json

dict_data = {'a': "haha", 'bb': 123, "ff": [1, "KK", 12]}
str_data = json.dumps(dict_data)
print(str_data)
print(isinstance(str_data, str))  #isinstance用法


new_str_data = '{"a": "haha", "bb": 123, "ff": [1, "KK", 12]}'
new_dict_data = json.loads(new_str_data)
print(new_dict_data)
print(isinstance(new_dict_data,dict))



