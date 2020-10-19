# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setting.py
   Description :   配置文件
   Author :        JHao
   date：          2019/2/15
-------------------------------------------------
   Change Activity:
                   2019/2/15:
-------------------------------------------------
"""

BANNER = r"""
****************************************************************
*** ______  ********************* ______ *********** _  ********
*** | ___ \_ ******************** | ___ \ ********* | | ********
*** | |_/ / \__ __   __  _ __   _ | |_/ /___ * ___  | | ********
*** |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | | ********
*** | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___  ****
*** \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____/ ****
****                       __ / /                          *****
************************* /___ / *******************************
*************************       ********************************
****************************************************************
"""

# ############### server config ###############
# HOST = "localhost"
HOST = "0.0.0.0"

PORT = 5010

# ############### database config ###################
# db connection uri
# example:
#      Redis: redis://:password@ip:port/db
#      Ssdb:  ssdb://:password@ip:port
DB_CONN = 'redis://:root@127.0.0.1:6379/1'

# proxy table name
TABLE_NAME = 'use_proxy'


# ###### config the proxy fetch function ######
PROXY_FETCHER = [
   #  "freeProxy01",   # 无忧代理, 20个 几乎没有能用的
   #  # "freeProxy02",  # ---代理66(count: 数量), 无返回结果
   #  # "freeProxy03",  # ---西刺代理(pagecount=10), 无法访问
   #  "freeProxy04",   # 全网代理guobanjia, 10个
   #  "freeProxy05",   # 快代理(page_count=20/3680, 15个/page) **
   # #  "freeProxy06",   # 码农代理coderbusy, country=cn, 106个 好站 **   连接失败, 暂未找到原因. 找到原因: 没加请求头
   #  "freeProxy07",   # 云代理(pagecount=7, 共100个)
   #  # "freeProxy08",  # ---IP海, 网站到期停机
   #  "freeProxy09",   # 免费代理库(pagecount=8/8, country=中国, 15个/page)  **
   # #  "freeProxy10",   # |||gfw
   # #  "freeProxy11",   # |||gfw
   # #  "freeProxy12",   # |||gfw
   # #  "freeProxy13",   # ---齐云代理, 无法访问
   #  "freeProxy14",   # 89免费代理(maxpage=20/unknow, 15个/page)   **
   #  "freeProxy15",   # 西拉免费代理(pagecount=20/2000, 50个/page, 普通|http)  **

   # 注释掉上面所有, 只用一个
   "freeProxy06",   # 码农代理coderbusy, country=cn, 106个 好站 **   
]

# ############# proxy validator #################
# VERIFY_URL = "http://www.baidu.com"
VERIFY_URL = "http://httpbin.org/ip"

VERIFY_TIMEOUT = 10

MAX_FAIL_COUNT = 0  # default 0


# ############# scheduler config #################

# Set the timezone for the scheduler forcely (optional)
# If it is running on a VM, and 
#   "ValueError: Timezone offset does not match system offset" 
#   was raised during scheduling.
# Please uncomment the following line and set a timezone for the scheduler.
# Otherwise it will detect the timezone from the system automatically.

# TIMEZONE = "Asia/Shanghai"
