# -*- coding:utf-8 -*-
# author:yangcong
# datetime:2020/5/13 10:57 下午
# software: PyCharm
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from basics.yapi import Yapi


def job():
    yapi = Yapi()
    yapi.get_update()
    yapi.get_api()
    yapi.requests_api()


scheduler = BlockingScheduler()
# 每隔 5秒钟 运行一次 job 方法
scheduler.add_job(job, 'interval', seconds=5, args=[])
# 在 2019-08-29 22:15:00至2019-08-29 22:17:00期间，每隔1分30秒 运行一次 job 方法
# scheduler.add_job(job, 'interval', minutes=1, seconds=30, start_date='2019-08-29 22:15:00',
#                   end_date='2019-08-29 22:17:00', args=['job2'])

scheduler.start()
