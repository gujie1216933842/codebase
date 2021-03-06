'''
1. 三次握手
   每当建立tcp/ip连接的时候,都要经历3次握手,这是为了保证建立一个可靠的连接

2. 四次挥手
   四次挥手的作用:断开连接,之所以要断开连接,是因为tcp/ip协议是要占用端口的,而计算机的端口是有限的,所以一次完成
                传输后,要断开连接,断开连接的方式就是4次挥手

3. ARP协议
  地址解析协议(Address Resolution Protocol): 根据IP地址获取物理地址的一个TCP/IP协议


9. http和https
http:超文本传输协议,http协议以明文的方式发送内容,不提供任何方式的数据加密,如果攻击者截取了web浏览器和网站服务器
     之间的传输报文,就可以直接读懂其中的信息,因此http协议不适合传输一些敏感信息(比如:银行卡卡号,支付密码等)

https:为了数据的传输安全,https在http的基础上加入了ssl协议,ssl依靠证书来验证服务器的身份,
      并未浏览器和服务器之间的通信加密

'''

