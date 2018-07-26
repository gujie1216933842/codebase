from concurrent.futures import ProcessPoolExecutor

import multiprocessing

#多进程编程,使用进程池

import time
def get_html(n):
    time.sleep(n)
    print('sub_progress success')
    return n


if __name__ == "__main__":

    print('cup:{}'.format(multiprocessing.cpu_count()))
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html,args=(3,))

    #等待所有任务完成
    pool.close()
    pool.join()
    print(result.get())