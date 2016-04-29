# -*- coding: utf-8 -*-

from managerlib.common.exceptions import LockTimeout, MessageTimeout
from managerlib.urls.flask import *

from confcenter.platform.http_flask_config import flaskAddExecutor,flaskDelExecutor,flaskListExecutor,\
    flaskGetConfig,flaskSetConfig
    
def flaskUrl2View():
    url2view = {}
    
    url2view.update({strExecutorAdd:flaskAddExecutor})
    url2view.update({strExecutorDel:flaskDelExecutor})
    url2view.update({strExecutorList:flaskListExecutor})
    url2view.update({strConfigSet:flaskSetConfig})
    url2view.update({strConfigGet:flaskGetConfig})
    
    return url2view

