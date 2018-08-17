import re
'''compile和findall一起用'''
str = 'asdas12asafsef1\n' \
      '2121asedas55'
pattern = re.compile('\d')
items = re.findall(pattern, str)
print(items)

