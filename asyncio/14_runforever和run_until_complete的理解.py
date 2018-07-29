'''
run_until_completed()  运行完某个协程后停止

底层源码也是运行run_forever,只不过加了add_done_callback,回调执行完之后  执行 loop.stop()

run_forever  整个循环一直运行,不会停止

'''


