# -*- coding: utf-8 -*-

from managerlib.db.table.lock.mysql import getdb
from managerlib.advanced.cachedb import CacheDb
from managerlib.advanced.cacheuser import CacheUser
from managerlib.advanced.cacheconsistency import CacheConsistency
from managerlib.advanced.cachequeue import CacheQueue

GLOBAL_USER_DB = CacheDb(getdb)

GLOBAL_USER_TOKEN = CacheUser()
GLOBAL_USER_CONSISTENCY = CacheConsistency()

USER_CONSISTENCY_DIR = CacheQueue()

strTimeStamp = 'timestamp'
