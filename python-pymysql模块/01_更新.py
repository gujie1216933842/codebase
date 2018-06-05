import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123',
    db='python_spider',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()  # 最终返回数据类型元组
# cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)  #最终返回数据类型字典

# 查询数据
sql = "update my_test set name  = %s "
# data = (1)
cursor.execute(sql, ('乔布斯'))  # 如果没有参数就不传,大于等于两个需要写成tuple形式

print('行数:%s' % cursor.rowcount)
affect = cursor.rowcount

cursor.close()
connect.close()


'''
CREATE TABLE `my_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `name` varchar(200) NOT NULL DEFAULT '' COMMENT '手机名字',
  `price` decimal(22,2) NOT NULL DEFAULT '0.00' COMMENT '手机价格',
  `good_comment` int(11) NOT NULL DEFAULT '0' COMMENT '好评数',
  `center_comment` int(11) NOT NULL DEFAULT '0' COMMENT '中评数',
  `bad_comment` int(11) NOT NULL DEFAULT '0' COMMENT '差评数',
  `raw_add_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '记录添加时间',
  `raw_update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录修改时间',
  `delete_flag` tinyint(2) NOT NULL DEFAULT '0' COMMENT '记录是否删除标记',
  PRIMARY KEY (`id`),
  KEY `idx_price` (`price`),
  KEY `idx_good_comment` (`good_comment`),
  KEY `idx_center_comment` (`center_comment`),
  KEY `idx_bad_comment` (`bad_comment`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
'''
