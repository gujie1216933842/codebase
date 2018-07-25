'''

crontab表达式添加在
/var/spool/cron/   目录文件下
如果是root用户,会有一个root文件
把crontab表达式添加进root文件即可

在每天19:00和20:00之间每分钟发送邮件
* 19-20 * * * curl "http://47.97.165.75:9000/mail/send/"

每天10:00执行一次
30 10 * * * python3 /home/gujie/project/codebase/scripts/sz_stock_update.py


实现Linux定时任务有:cron、anacron、at等，这里主要介绍cron服务。

名词解释：

   cron是服务名称，crond是后台进程，crontab则是定制好的计划任务表。

软件包安装：

要使用cron服务，先要安装vixie-cron软件包和crontabs软件包，两个软件包作用如下：

vixie-cron软件包是cron的主程序。
crontabs软件包是用来安装、卸装、或列举用来驱动 cron 守护进程的表格的程序。

查看是否安装了cron软件包: rpm -qa|grep vixie-cron

查看是否安装了crontabs软件包:rpm -qa|grep crontabs

如果没有安装，则执行如下命令安装软件包(软件包必须存在)
rpm -ivh vixie-cron-4.1-54.FC5*
rpm -ivh crontabs*

如果本地没有安装包，在能够连网的情况下可以在线安装

yum install vixie-cron
yum install crontabs

查看crond服务是否运行：

pgrep crond

或

/sbin/service crond status

或

ps -elf|grep crond|grep -v "grep"



crond服务操作命令:

/sbin/service crond start //启动服务
/sbin/service crond stop //关闭服务
/sbin/service crond restart //重启服务
/sbin/service crond reload //重新载入配置



配置定时任务：

cron有两个配置文件，一个是一个全局配置文件（/etc/crontab），是针对系统任务的；一组是crontab命令生成的配置文件（/var/spool/cron下的文件），是针对某个用户的.定时任务配置到任意一个中都可以。

查看全局配置文件配置情况: cat /etc/crontab

---------------------------------------------
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/

# run-parts
01 * * * * root run-parts /etc/cron.hourly
02 4 * * * root run-parts /etc/cron.daily
22 4 * * 0 root run-parts /etc/cron.weekly
42 4 1 * * root run-parts /etc/cron.monthly
----------------------------------------------

查看用户下的定时任务:crontab -l或cat /var/spool/cron/用户名

crontab任务配置基本格式：
*   *　 *　 *　 *　　command
分钟(0-59)　小时(0-23)　日期(1-31)　月份(1-12)　星期(0-6,0代表星期天)　 命令

第1列表示分钟1～59 每分钟用*或者 */1表示
第2列表示小时1～23（0表示0点）
第3列表示日期1～31
第4列表示月份1～12
第5列标识号星期0～6（0表示星期天）
第6列要运行的命令

在以上任何值中，星号（*）可以用来代表所有有效的值。譬如，月份值中的星号意味着在满足其它制约条件后每月都执行该命令。
整数间的短线（-）指定一个整数范围。譬如，1-4 意味着整数 1、2、3、4。
用逗号（,）隔开的一系列值指定一个列表。譬如，3, 4, 6, 8 标明这四个指定的整数。
正斜线（/）可以用来指定间隔频率。在范围后加上 /<integer> 意味着在范围内可以跳过 integer。譬如，0-59/2 可以用来在分钟字段定义每两分钟。间隔频率值还可以和星号一起使用。例如，*/3 的值可以用在月份字段中表示每三个月运行一次任务。
开头为井号（#）的行是注释，不会被处理。



例子：

0 1 * * * /home/testuser/test.sh
每天晚上1点调用/home/testuser/test.sh

*/10 * * * * /home/testuser/test.sh
每10钟调用一次/home/testuser/test.sh

30 21 * * * /usr/local/etc/rc.d/lighttpd restart
上面的例子表示每晚的21:30重启apache。

45 4 1,10,22 * * /usr/local/etc/rc.d/lighttpd restart
上面的例子表示每月1、10、22日的4 : 45重启apache。

10 1 * * 6,0 /usr/local/etc/rc.d/lighttpd restart
上面的例子表示每周六、周日的1 : 10重启apache。

0,30 18-23 * * * /usr/local/etc/rc.d/lighttpd restart
上面的例子表示在每天18 : 00至23 : 00之间每隔30分钟重启apache。

0 23 * * 6 /usr/local/etc/rc.d/lighttpd restart
上面的例子表示每星期六的11 : 00 pm重启apache。

* */1 * * * /usr/local/etc/rc.d/lighttpd restart
每一小时重启apache

* 23-7/1 * * * /usr/local/etc/rc.d/lighttpd restart
晚上11点到早上7点之间，每隔一小时重启apache

0 11 4 * mon-wed /usr/local/etc/rc.d/lighttpd restart
每月的4号与每周一到周三的11点重启apache

0 4 1 jan * /usr/local/etc/rc.d/lighttpd restart
一月一号的4点重启apache

*/30 * * * * /usr/sbin/ntpdate 210.72.145.44
每半小时同步一下时间


配置用户定时任务的语法：

crontab [-u user]file

crontab [-u user] [-l| -r | -e][-i]

参数与说明：

crontab -u//设定某个用户的cron服务

crontab -l//列出某个用户cron服务的详细内容

crontab -r//删除没个用户的cron服务

crontab -e//编辑某个用户的cron服务



例子：

假设当前用户是root，要建立root用户的定时任务

crontab -e

选择编辑器，编辑定时任务(这里假设是编辑器是vi)

按i进入编辑模式

0 1 * * * /root/test.sh

按esc退出编辑模式进入普通模式，输入:x或:wq保存退出

查看刚刚输入的定时任务

crontab -l 或 cat /var/spool/cron/root

根用户以外的用户可以使用 crontab 工具来配置 cron 任务。所有用户定义的 crontab 都被保存在 /var/spool/cron 目录中，并使用创建它们的用户身份来执行。要以某用户身份创建一个 crontab 项目，登录为该用户，然后键入 crontab -e 命令，使用由 VISUAL 或 EDITOR 环境变量指定的编辑器来编辑该用户的 crontab。该文件使用的格式和 /etc/crontab 相同。当对 crontab 所做的改变被保存后，该 crontab 文件就会根据该用户名被保存，并写入文件 /var/spool/cron/username 中。
      cron 守护进程每分钟都检查 /etc/crontab 文件、etc/cron.d/ 目录、以及 /var/spool/cron 目录中的改变。如果发现了改变，它们就会被载入内存。这样，当某个 crontab 文件改变后就不必重新启动守护进程了。

重启crond：

/sbin/service crond restart

查看cron服务是否起作用：

如果我们要查看定时任务是否准时调用了可以/var/log/cron中的运行信息

cat /var/log/cron

或

grep .*\.sh /var/log/cron

搜索.sh类型文件信息
或

sed -n '/back.*\.sh/p' /var/log/cron
格式sed -n '/字符或正则表达式/p' 文件名

我们在日志中查看在约定的时间是否有相应的调用信息，调用信息类似：

Sep 19 1:00:01 localhost crond[25437]: (root) CMD (/root/test.sh)

查看shell脚本是否报错：

如果/var/log/cron中准时调用了shell脚本，而又没有达到预期结果，我们就要怀疑shell脚本是否出错

cat /var/spool/mail/用户名

例子：

cat /var/spool/mail/root



test.sh

-------------------------

#!/bin/sh

echo "$(date '+%Y-%m-%d %H:%M:%S') hello world!" >> /root/test.log

-------------------------

要追踪shell调用的全过程：

bash -xv test.sh 2>test.log

test.sh的调用过程都会写到test.log中

或

改写test.sh



-------------------------

#!/bin/sh

set -xv

echo "$(date '+%Y-%m-%d %H:%M:%S') hello world!" >> /root/test.log

-------------------------

sh ./test.sh 2>tt.log








'''