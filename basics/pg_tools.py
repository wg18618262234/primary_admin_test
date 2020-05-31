# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/5/13 7:42 下午
# software: PyCharm
import psycopg2, time
from psycopg2.extras import RealDictCursor
from config import PGDB_CONFIG as pgc
from basics.log import logging
from basics.time_conversion import date_now


class pgdb():
    def __init__(self):
        self.conn = psycopg2.connect(database=pgc.get('database'), user=pgc.get('user'),
                                     password=pgc.get('password'), host=pgc.get('host'), port=pgc.get('port'))

    def insert(self, table_name, data=None, **dict):
        if dict:
            data = dict
        cur = self.conn.cursor()
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(list(data.keys()))
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table_name, columns, placeholders)
        logging.info('sql: ' + sql + ' % (' + str(list(data.values())) + ')')
        cur.execute(sql, list(data.values()))
        rowcount = cur.rowcount
        logging.info('受影响行数：' + str(rowcount))
        self.conn.commit()
        self.conn.close()
        return {'受影响行数': str(rowcount)}

    def select(self, table_name, where_sql=None, order_by=None, limit=None):
        sql = '''SELECT * FROM {}'''.format(table_name)
        if not where_sql is None:
            sql += ' WHERE ' + where_sql
        if not order_by is None:
            sql += ' ORDER BY ' + order_by
        if not limit is None:
            sql += ' LIMIT ' + str(limit)
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        logging.info(sql)
        cur.execute(sql)
        result = cur.fetchall()
        self.conn.close()
        return result

    def update(self, table_name, id, data=None, **dict):
        if dict:
            data = dict
        columns = ' = %s,'.join(list(data.keys())) + ' = %s'
        sql = "UPDATE %s SET %s WHERE id = %s" % (table_name, columns, id)
        cur = self.conn.cursor()
        logging.info('sql: ' + sql + ' % (' + str(list(data.values())) + ')')
        cur.execute(sql, list(data.values()))
        rowcount = cur.rowcount
        logging.info('受影响行数：' + str(rowcount))
        self.conn.commit()
        self.conn.close()
        return {'受影响行数': str(rowcount)}

    def delete(self, table_name, id):
        sql = "DELETE FROM %s WHERE id = %s" % (table_name, id)
        cur = self.conn.cursor()
        logging.info('sql: ' + sql)
        cur.execute(sql)
        rowcount = cur.rowcount
        logging.info('受影响行数：' + str(rowcount))
        self.conn.commit()
        self.conn.close()
        return {'受影响行数': str(rowcount)}


if __name__ == '__main__':
    db = pgdb()
    # db.insert(table_name='api_trends', _id=11, content='qwerrr')
    # data = {"_id": "11", "content": "qwerrr"}
    # db.update('api_trends', data, 6492)
    # db.insert(table_name='api_trends', data=data)
    # db.select(table_name='api_trends', where_sql='_id = 2')
    # db.select(table_name='api_trends')
