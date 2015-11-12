#!/usr/bin/env python
# encoding: utf-8
import urllib2,urllib,os,re,socket,requests,json,time
socket.setdefaulttimeout(50)

"""
@version: 1.0
@author: hiphp
@license: Apache Licence 
@contact: hi_php@163.com
@site: wuwenfu.cn
@software: PyCharm Community Edition
@file: shuatiezi.py
@time: 2015/11/12 20:22

自动回复帖子。


"""
def post(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    #enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()

def post_html(url):
    html = ''
    request = urllib2.Request(url)
    #这里依次添加数据。
    request.add_header('Host', 'bbs.luanren.com')
    request.add_header("User_Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0")
    request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    request.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    request.add_header("Referer","http://bbs.luanren.com/forum.php?mod=viewthread&tid=5235351&extra=page%3D1")
    request.add_header("Cookie","你自己的")
    request.add_header("Content-Type","application/x-www-form-urlencoded")
    msg = u'再顶一次。你写的文章真棒，我来帮你顶顶。呵呵。'
    msg = msg.encode('gbk')

    data = {'message':msg,'posttime':time.time(),'formhash':'3a0144be','usesig':1,'connect_publish_t':0}
    data = urllib.urlencode(data)
    # response = urllib.urlopen(request,data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(request, data)
    html = response.read()
    html = unicode(html,'GBK').encode('UTF-8')
    # print(html)

    # try:
    #     html = urllib2.urlopen(url).read()
    # except Exception,e:
    #     print(u'打开网页%s错误:%s'% (url,e.message))
    # return html

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # url = 'http://bbs.luanren.com/forum.php?mod=post&action=reply&fid=50&tid=5235351&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
    url = "http://bbs.luanren.com/forum.php?mod=post&action=reply&fid=50&tid=5235245&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"

    # url = "http://bbs.luanren.com/forum.php?mod=viewthread&tid=5235225&extra=page%3D1"

    #随机抽几个帖子，进行评论。5235225  我们选择10篇文章。进行评论。

    links = ['http://bbs.luanren.com/forum.php?mod=post&action=reply&fid=50&tid=%s&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1' % i for i in xrange(5235200,5235205)]
    for link in links:
        print(link)
        time.sleep(5)
        #评论的地址
        # linkform = link+'&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'
        post_html(link)

    # post_html(url)
    pass