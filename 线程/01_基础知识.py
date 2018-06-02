'''
网上有争论,python多线程是鸡肋,那么到底python的多线程有没有用
争论的核心,因为python解释器中GIL(全局解释器锁的存在),导致python的多线程在同一时刻只会有一条线程跑在cpu中,其他线程都在睡觉,
我们需要怎么理解

python确实由于GIL的存在,名义上的多线程,实际单线程,
但是不能理解为python的多线程是没用的
这里具体要看程序是什么样的,
如果是一个以计算为主的程序(专业:cpu密集型),python这点确实比较吃亏,每一个线程一次在cpu中跑一遍,这就相当于单线程了,甚至比单线程还要慢
(因为cpu线程的上下文切换也需要开销的)

但是如果是一个以磁盘或者网络为主的程序(专业称之为IO密集型)就不同了,
一个线程处在IO等待的时候,另一个线程就可以再cpu中跑,因为有时候cpu是闲着没事干,所有线程都等待着IO,
这种情况下,python的多线程就是同时了,能提高效率,而单线程的话还是一个个一次等待

我们知道IO的速度比起cpu速度来,慢到令人发指,python的多线程利用了IO与cpu之间过大的速度差发挥作用,
比如应用场景:多线程网络传输,多线程往不同目录写文件,爬虫

话说回来,cpu密集型程序用python来做,本身就是不合适的,和C,go,java比,性能差好多
扩展思路,可以用C写一个多线程,用python来调用,那样速度是最快的
我们之所以用python的原因是,开发效率高





理解GIL
python设计之初,为了数据安全做的决定

python的某个线程想要执行,必须先难道GIL我们可以把GIL看成通行证,并且在python的一个进程中,同一时刻的GIL只有一个
拿不到通行证的线程就不允许进程cpu执行





'''

'''
线程和进程一样,都是执行多任务的标记

进程:把一坨写好的代码执行起来,在内存中分配一块地址,整个这个环境称为进程(占用资源的环境)
     进程是资源分配的单位
线程:进程运行起来了之后,进程里面需要执行代码的执行流程  
     线程是cpu调度的单位,(理解:代码执行流程的核心就是过cpu,由cpu调度)
     多线程就是在同一个进程分配的资源环境内,cpu再次或多次启动调用代码
     进程开始运行后cpu第一次调度的线程称之为主线程  
     子线程全部执行完之后,主线程才会结束


启动一个进程之后执行,其实就默认启动了一个线程




'''





