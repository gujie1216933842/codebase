'''
aysncio:python协程的一个框架,主要功能完成协程的调度,同时能够让我们在同步编程的时候还能像同步编码的方式来编写我们的异步代码


我们平时编写多线程和多进程代码的时候,线程代码和进程代码的调度有操作系统来完成,操作系统对于很多程序来说,都是一个黑盒,
操作系统在调度的过程中有非常多的逻辑,这些逻辑都是有操作系统完成的,不需要我们去接触操作系统的原理,所以操作系统本身的
调度过程对我们来说就是一个黑盒.

但是斜撑不一样,协程的编码方式,由我们阻塞的io的编码方式直接转化成异步非阻塞的编码方式,这是一个很大的转变,所以说
这些转变的过程中,我们不得不去了解协程的调度过程,这就加大了我们对协程的理解难度
但了解了协程的调度过程之后,我们可以知道,可以怎么去写协程的代码
我们了解协程的关键,就在于我们要了解协程的原理






'''