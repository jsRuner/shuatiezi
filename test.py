#!/usr/bin/env python
# encoding: utf-8
import urllib2,urllib,os,re,socket,requests,json,time,random
socket.setdefaulttimeout(50)

"""
@version: 1.0
@author: hiphp
@license: Apache Licence 
@contact: hi_php@163.com
@site: wuwenfu.cn
@software: PyCharm Community Edition
@file: test.py
@time: 2015/11/15 21:31
"""


def post_html(url):
    html = ''
    request = urllib2.Request(url)
    #这里依次添加数据。
    request.add_header('Host', 'bbs.luanren.com')
    request.add_header("User_Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0")
    request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    request.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    request.add_header("Referer","http://bbs.luanren.com/forum.php?mod=viewthread&tid=5235351&extra=page%3D1")
    request.add_header("Cookie","BUeE_8b1b_saltkey=e2AEWAeA; BUeE_8b1b_lastvisit=1447327136; BUeE_8b1b_lastact=1447416831%09forum.php%09ajax; pgv_pvi=6183887470; CNZZDATA1290563=cnzz_eid%3D108391050-1447330619-%26ntime%3D1447414881; BUeE_8b1b_client_created=1447330742; BUeE_8b1b_client_token=104CA1629085BEA374E5C0D770050FD9; BUeE_8b1b_ulastactivity=1447416625%7C0; BUeE_8b1b_auth=e0b4fbXbhjYMOjknj7PE6E6qkg8p68OWp0csBqFXoA2sJf07sIF5HYLWO%2FDIKx9Xu9j3MrqRc2h8j%2BPouSS%2BgA%2FGGiI; BUeE_8b1b_connect_login=1; BUeE_8b1b_connect_is_bind=1; BUeE_8b1b_connect_uin=104CA1629085BEA374E5C0D770050FD9; BUeE_8b1b_nofavfid=1; BUeE_8b1b_connect_last_report_time=2015-11-13; BUeE_8b1b_atarget=1; BUeE_8b1b_forum_lastvisit=D_50_1447333256D_207_1447416723; BUeE_8b1b_smile=2D1; BUeE_8b1b_security_cookiereport=a0ee7ggg3ynyeeI%2FLaHSO6pY%2Fa%2FrqmiCmzxFCm%2FRUSZjHr9%2BsJpK; BUeE_8b1b_onlineusernum=7032; BUeE_8b1b_sendmail=1; BAIDU_SSP_lcr=http://www.baidu.com/link?url=DO3F7RgmVmtvYq9qXxaXkssyFZC_nQrvsYK45KLmhtEjGU9-scyvMqFlZdbZwdYm&wd=&eqid=bc0d2f500000557e000000045645d32d; pgv_info=ssi=s3697179615; tjpctrl=1447418445655; BUeE_8b1b_st_p=140204%7C1447416644%7C57f9b86d79ab9bc30e85239943cbe1d5; BUeE_8b1b_viewid=tid_5235203; BUeE_8b1b_st_t=140204%7C1447416760%7Cd00dfa98702e712357a00409c0c0559c")
    request.add_header("Content-Type","application/x-www-form-urlencoded")
    msg = u'顶一下。写的不错，我来帮你顶顶。呵呵。顺便水一波经验。'
    msg = msg.encode('gbk')

    data = {'message':msg,'posttime':time.time(),'formhash':'3a0144be','usesig':1,'connect_publish_t':0}
    data = urllib.urlencode(data)
    # response = urllib.urlopen(request,data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(request, data)
    html = response.read()
    html = unicode(html,'GBK').encode('UTF-8')

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':

    links = ['http://bbs.luanren.com/forum.php?mod=post&action=reply&fid=50&tid=%s&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1' % i for i in xrange(5235200,5235205)]
    ids = xrange(1,5)
    for id in ids:
        # id = random.randrange(4713560,5235200)
        id = id +4713561
        articleurl = "http://bbs.luanren.com/forum.php?mod=viewthread&tid=%s" % id
        commenturl = "http://bbs.luanren.com/forum.php?mod=post&action=reply&fid=50&tid=%s&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1" % id
        print(u"文章地址:%s" % articleurl)
        time.sleep(3)
        post_html(commenturl)