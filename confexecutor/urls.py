# -*- coding: utf-8 -*-

from managerlib.common.exceptions import LockTimeout, MessageTimeout
from managerlib.common.bufferedhttp import jresponse
from managerlib.urls.config import *
from confexecutor.http_config_center import centerGetConfig,centerPullExecutor,centerSetConfig

url2view = {}
url2view.update({strExecutorPull:centerPullExecutor})
url2view.update({strConfigGet:centerGetConfig})
url2view.update({strConfigSet:centerSetConfig})

def handlerequest(req):
    url = req.path
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    return url2view[url](req)
