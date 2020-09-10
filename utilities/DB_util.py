import pymysql
from pymysqlpool import connection
import conf.com_config


# 打开数据库连接
class MysqlUtil(object):

    def __init__(self):
        self.db = None
        self.get_cursor()

    def get_cursor(self):
        mysql_conf_list = conf.com_config.get_mysql_conf()
        self.db = pymysql.connect(host=mysql_conf_list[0],
                                  port=mysql_conf_list[1],
                                  user=mysql_conf_list[3],
                                  password=mysql_conf_list[5],
                                  db=mysql_conf_list[2],
                                  charset=mysql_conf_list[6])

    def mysql_driver(self, sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        data = cursor.execute(sql)
        # print("Database version : %s " % data)
        # 关闭数据库连接
        self.db.close()
        return data

    def connection_pool(self):
        '''
        建立连接池
        :return:  连接池
        '''
        pool = connection.MySQLConnectionPool(**self.config_database)
        pool.connect()
