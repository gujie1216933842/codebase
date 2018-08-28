s = b'\u4e2d\u6587\u5b57\u7b26'
print(s.decode('unicode_escape'))

ch_s = '中文字符'
print(ch_s.encode())


b_s =  b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6'
print(b_s.decode())