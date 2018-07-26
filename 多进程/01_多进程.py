from concurrent.futures import ProcessPoolExecutor

import multiprocessing

#多进程编程

import time
def get_html(n):
    time.sleep(n)
    print('sub_progress success')
    return n


if __name__ == "__main__":
    progress = multiprocessing.Process(target=get_html,args=(2,))
    print(progress.pid)
    progress.start()
    print(progress.pid)
    progress.join()
    print('main progress end')
