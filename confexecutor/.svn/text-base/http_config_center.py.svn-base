# -*- coding: utf-8 -*-

import json
import socket
from managerlib.common.bufferedhttp import jresponse
from managerlib.utils.uuid import loadUuid
from confexecutor.libconfig.libauth import libGetAuth,libSetAuth
from confexecutor.libconfig.libcache import libGetCache,libSetCache
from confexecutor.libconfig.libconcurrency import libGetConCurrency,libSetConCurrency
from confexecutor.libconfig.libproxy import libGetProxy,libSetProxy
from confexecutor.libconfig.libstorage import libGetStorage,libSetStorage

class2func = {'auth':libSetAuth,
              'cache':libSetCache,
              'concurrency':libSetConCurrency,
              'proxy':libSetProxy,
              'storage':libSetStorage}

def centerPullExecutor(request):
    host_info = {'uuid':loadUuid(),
                 'name':socket.gethostname()}
    return jresponse('0',json.dumps(host_info),request,200)

def centerGetConfig(request):
    
    attrs = {}
    attrs.update({'auth':libGetAuth()})
    attrs.update({'cache':libGetCache()})
    attrs.update({'concurrency':libGetConCurrency()})
    attrs.update({'proxy':libGetProxy()})
    attrs.update({'storage':libGetStorage()})
    
    return jresponse('0',json.dumps(attrs),request,200)

def centerSetConfig(request):
    param = json.loads(request.body)
    attrs = param.get('confAttrs')
    
    for classtype,confdict in attrs.items():
        if classtype not in class2func:
            continue
        class2func[classtype](confdict)
        
    return jresponse('0','',request,200)
