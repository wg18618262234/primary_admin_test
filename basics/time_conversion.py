# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/5/14 11:19 上午
# software: PyCharm

import time


def timestamp_to_date(time_stamp):
    '''
    将时间戳转换为指定日志
    :param time_stamp: timestamp
    :return: %Y-%m-%d %H:%M:%S
    '''
    if time_stamp is None:
        return None
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_stamp))
    return date


def date_to_timestamp(date:str):
    '''
    将日志转换为时间戳
    :param date: %Y-%m-%d %H:%M:%S
    :return: timestamp
    '''
    if date is None:
        return None
    timeArray = time.strptime(str(date), "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return timestamp


def date_now():
    '''
    现在时间日期
    :return: %Y-%m-%d %H:%M:%S
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == '__main__':
    t = timestamp_to_date(time.time())
    print(t)
    t1 = date_to_timestamp('2020-05-13 16:51:09')
    print(t1)
    print(time.time())
    print(date_now())
