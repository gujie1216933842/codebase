'''
tcp/ip 协议:  表示一堆互联网协议(成千上百ftp/stmp/.....)的集合的总称  其中两个重要的协议tic和ip
协议:用来完成进程中通信的协议

网络协议分的层次
按四层:实际代码开发
    应用层
    传输层
    网络层
    链路层

按七层分:理论上
    应用层
    表示层
    会话层

    传输层

    网络层

    数据链路层
    物理层


端口:用来区分进程


ip地址:用来标记网络上的一台电脑
以c类ip地址为例,
xxx.xxx.xxx.0~255
其中有两个ip地址不能用
0和255
xxx.xxx.xxx.0  表示网络号
xxx.xxx.xxx.255 表示广播地址

ipv4  前几年全球已经瓜分完了,国内暂时还用的是ipv4
现在新的ipv6:未来用的ip地址


私有ip:只能在局域网内使用
公有ip:能上网的ip

tcp和udp的区别
tcp慢,不丢数据
udp块,丢数据,在局域网上,udp一般也不会丢包



tcp三次握手
1.tcp服务器进程先创建一个传输控制块tcb,时刻准备接收客户端进程的连接请求,此时服务器进入监听状态
2.tcp客户端也先创建一个传输模块tcb,然后向服务器发送传输报文,报文不带数据
3.tcp服务器接收到请求报文后,如果同意连接,则发布确认报文,报文不带数据
4.tcp客户端进程接收到确认后,还要向服务器给出确认,此时可携带数据,但如果不携带数据则不消耗序号
5.当服务器收到客户端的确认后进入可通信的状态


tcp三次握手
第一次握手:主机A发送码syn=1,随机产生seq number = 1234567的数据包到主机B , 主机B由syn = 1,主机A要求建立连接
第二次握手:主机B收到请求后要确认联机信息,向主机A发送 ack number = (主机A的seq+1),syn = 1 ,ack=1,随机产生seq=7654321的包
第三次握手:主机A收到后检查ack number是否正确,即第一次发送的seq number+1,以及ack是否为1,
          若正确,主机A会再发送ack number = (主机B的seq+1),ack=1,主机B收到后确认seq值与ack=1则连接建立成功

完成三次握手,主机A与主机B开始传送数据


实例:

IP 192.168.1.116.3337 > 192.168.1.123.7788: S 3626544836:3626544836
IP 192.168.1.123.7788 > 192.168.1.116.3337: S 1739326486:1739326486 ack 3626544837
IP 192.168.1.116.3337 > 192.168.1.123.7788: ack 1739326487,ack 1

第一次握手：192.168.1.116发送位码syn＝1,随机产生seq number=3626544836的数据包到192.168.1.123,192.168.1.123由SYN=1知道192.168.1.116要求建立联机;

第二次握手：192.168.1.123收到请求后要确认联机信息，向192.168.1.116发送ack number=3626544837,syn=1,ack=1,随机产生seq=1739326486的包;

第三次握手：192.168.1.116收到后检查ack number是否正确，即第一次发送的seq number+1,以及位码ack是否为1，若正确，192.168.1.116会再发送ack number=1739326487,ack=1，192.168.1.123收到后确认seq=seq+1,ack=1则连接建立成功。



网络4层
应用层,传输层,网络层,链路层
网络七层
(应用层,表示层,会话层),传输层,网络层,(数据链路层,物理层)














'''