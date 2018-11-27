# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from pymysql import *
import pymysql
import time


# 在数据库中创建一个db4数据库，user表(表中只有自增长的id和唯一索引的user字段)
def random_username():
    db = pymysql.connect(host='localhost', user='root',
                         password='123456', database='db4', charset='utf8')
    cur = db.cursor()
    user_choice1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    user_choice2 = '0123456789'
    # 单进程创建2500个随机用户名,多进程创建1w个随机用户名
    for x in range(2500):
        user1 = random.sample(user_choice1, 2)
        user2 = random.sample(user_choice2, 4)
        user3 = user1 + user2
        user4 = ''.join(user3)
        try:
            # 因为是唯一索引，如果数据库中存在这个用户名，就会抛异常
            sql1 = 'insert into user5(user) values ("%s") ' % user4
            cur.execute(sql1)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

# 测试代码


def text():
    db = pymysql.connect(host='localhost', user='root',
                         password='123456', database='db4', charset='utf8')
    cur = db.cursor()
    sql2 = 'select user from user5'
    cur.execute(sql2)
    a = cur.fetchall()
    b = set(a)
    if len(a) == len(b):
        print('没有重复的用户名')
    else:
        print('用户名有重复的')


# 上述生成随机用户名的函数用了一个for循环,时间复杂度为n,其余的语句时间复杂度都为
# 常数项,所以该函数的时间复杂度为n,生成10000个随机用户名耗时19s


# 四进程
from multiprocessing import Process
import os

# 子进程要执行的代码


def run_proc():
    global L
    L = []
    time1 = time.time()
    for x in range(4):
        p = Process(target=random_username)
        p.start()
        L.append(p)

# 多进程时间测试


def time1_code():
    time1 = time.time()
    run_proc()
    for x in L:
        x.join()
    time2 = time.time()
    t = int(time2 - time1)
    print('多进程程序耗时%ds' % t)

# 单进程时间测试


def time2_code():
    time1 = time.time()
    random_username()
    time2 = time.time()
    t = int(time2 - time1)
    print('单进程程序耗时%ds' % t)


time1_code()
time2_code()
text()
