# coding:utf-8
import pymongo
import pymysql
from pymysqlpool import connection
import conf.com_config
import pandas


# 打开数据库连接
class MysqlUtil(object):

    def __init__(self):
        self.mysql_conf_list = conf.com_config.get_mysql_conf()
        self.db = self.get_cursor()
        self.pool = self.get_connection_pool()

    def get_cursor(self):
        # mysql_conf_list = conf.com_config.get_mysql_conf()
        db = pymysql.connect(host=self.mysql_conf_list[0],
                             port=int(self.mysql_conf_list[1]),
                             user=self.mysql_conf_list[3],
                             password=self.mysql_conf_list[4],
                             db=self.mysql_conf_list[2],
                             charset=self.mysql_conf_list[5])
        return db

    def mysql_driver(self, sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        data = cursor.execute(sql)
        # print("Database version : %s " % data)
        # 关闭数据库连接
        self.db.close()
        return data

    def get_connection_pool(self):
        '''
        建立连接池
        :return:  连接池
        '''

        pool = connection.MySQLConnectionPool(
            pool_name="test_pool",
            max_pool_size=30,
            pool_resize_boundary=48,
            host=self.mysql_conf_list[0],
            port=int(self.mysql_conf_list[1]),
            user=self.mysql_conf_list[3],
            password=self.mysql_conf_list[4],
            db=self.mysql_conf_list[2],
            charset=self.mysql_conf_list[5])

        return pool

    def pool_mysql_driver(self, sql):
        conn = self.pool.borrow_connection()
        data = pandas.read_sql(sql, conn)
        self.pool.return_connection(conn)
        return data


class MongoUtil(object):

    def __init__(self):
        self.mongo_conf_list = conf.com_config.get_mongo_conf()
        self.db = self.get_cursor()

    def get_cursor(self):
        client = pymongo.MongoClient(self.mongo_conf_list[0])
        db = client[self.mongo_conf_list[1]]
        return db

    def mongo_driver(self, col, query):
        mycol = self.db[col]
        data = mycol.find(query)
        return data


a = MysqlUtil()
data = a.pool_mysql_driver("select id from map;")
print(data["id"].values)
