# -*- coding: utf-8 -*-

from managerlib.common.bufferedhttp import jresponse
from confcenter.platform.flask_urls import flaskUrl2View

url2view = {}
url2view.update(flaskUrl2View())

def handlerequest(req):

    url = req.path
    print url
    if url not in url2view:
        return jresponse('-1','url error',req,404)
    if url.startswith('/cloudfs'):
        return url2view[url](req)
    else: 
        return url2view[url](req)


