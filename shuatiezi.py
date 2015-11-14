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

2015年11月13日 20:18:14
自动发帖子。

针对六安人论坛。




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

#发布帖子。
def post_article(url):
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
    title = u'皖西水友到此一游'
    title = title.encode('gbk')

    msg = u'毕业2年了，来看看，发个帖子，给六安人论坛助力'
    msg = msg.encode('gbk')

    data = {'message':msg,'posttime':time.time(),'formhash':'3a0144be','wysiwyg':1,'subject':title,'allownoticeauthor':1,'usesig':1,'connect_publish_t':0,'uploadalbum':8056,'newalbum':'testest'}

    data = urllib.urlencode(data)
    # response = urllib.urlopen(request,data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(request, data)
    html = response.read()
    html = unicode(html,'GBK').encode('UTF-8')
    print(html)

    # try:
    #     html = urllib2.urlopen(url).read()
    # except Exception,e:
    #     print(u'打开网页%s错误:%s'% (url,e.message))
    # return html

#抓去QQ空间的数据，说说，目标QQ是 落定 787560576

def post_qzone(url):
    html = ''
    request = urllib2.Request(url)
    #这里依次添加数据。
    request.add_header('Host', 'taotao.qq.com')
    request.add_header("User_Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0")
    request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    request.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    request.add_header("Referer","http://ctc.qzs.qq.com/qzone/app/mood_v6/html/index.html")
    request.add_header("Cookie","pt2gguin=o0540045865; ptcz=aa8d3f9f92aa78b56b04a724dcb132acb026a5dbe4e2174fb2f546f818d321d9; pgv_pvi=8711576576; pgv_pvid=2428832088; RK=qBEaMhi5Pj; skey=@Lm30JYIsc; pt_clientip=aac03cbac065ddd1; pt_serverip=43c80abf06596c2d; uin=o0540045865; ptisp=ctc; qzone_check=540045865_1447418270; rv2=800573FBFE2CCCC0D3052FE624626A2540B8FB8E04DA839819; property20=6130E6A08FF8F5C567EF588DB734071E97694BCFBC47E798E14DC216CF4DC2773D3A19203C428E55; pgv_info=ssid=s8111972637")

    # title = u'皖西水友到此一游'
    # title = title.encode('gbk')
    #
    # msg = u'毕业2年了，来看看，发个帖子，给六安人论坛助力'
    # msg = msg.encode('gbk')
    #
    # data = {'message':msg,'posttime':time.time(),'formhash':'3a0144be','wysiwyg':1,'subject':title,'allownoticeauthor':1,'usesig':1,'connect_publish_t':0,'uploadalbum':8056,'newalbum':'testest'}
    #
    # data = urllib.urlencode(data)
    # response = urllib2.urlopen(request)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(request)
    html = response.read()
    html = unicode(html,'GBK').encode('UTF-8')
    print(html)

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
    url = "http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=787560576&ftype=0&sort=0&pos=0&num=20&replynum=100&g_tk=814364931&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1"
    post_qzone(url)
    exit()

    #谈天说地区
   #url = "http://bbs.luanren.com/forum.php?mod=post&action=newthread&fid=207&extra=&topicsubmit=yes"
    #互助区
    url = "http://bbs.luanren.com/forum.php?mod=post&action=newthread&fid=45&extra=&topicsubmit=yes"
    post_article(url)

    exit()


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