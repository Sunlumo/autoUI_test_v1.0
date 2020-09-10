import pymysql
from pymysqlpool import connection
import conf.com_config


# �����ݿ�����
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
        # ʹ�� cursor() ��������һ���α���� cursor
        cursor = self.db.cursor()
        # ʹ�� execute()  ����ִ�� SQL ��ѯ
        data = cursor.execute(sql)
        # print("Database version : %s " % data)
        # �ر����ݿ�����
        self.db.close()
        return data

    def connection_pool(self):
        '''
        �������ӳ�
        :return:  ���ӳ�
        '''
        pool = connection.MySQLConnectionPool(**self.config_database)
        pool.connect()
