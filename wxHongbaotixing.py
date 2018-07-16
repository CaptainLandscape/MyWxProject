#coding=utf-8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
import importlib
importlib.reload(sys)
import os
import requests
'''
这是几个免费的key
8edce3ce905a4c1dbb965e6b35c3834d
eb720a8970964f3f855d863d24406576
1107d5601866433dba9599fac1bc0083
71f28bf79c820df10d39b4074345ef8c
'''
KEY = 'bd63c75752ba472080671663272f7473'

# 请求图灵机器人并得到返回消息
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'

    data = {
        'key': KEY,
        'info': msg,
        'userid': 'Gerald'
    }

    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
# 这是微信文本回复
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    default_reply = 'I received: ' + msg['Text']
    # 此处调用图灵机器人返回的消息
    reply = get_response(msg['Text'])
    return reply or default_reply

# 这是微信群被@之后回复
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        reply = get_response(msg['Text'])
        itchat.send(u'@%s\u2005: %s' % (msg['ActualNickName'], reply), msg['FromUserName'])

@itchat.msg_register(NOTE,isGroupChat=True)#监听群内红包消息
def receive_red_packet(msg):
    if u"收到红包" in msg['Content']:
        groups  = itchat.get_chatrooms(update=True)
        users = itchat.search_chatrooms(name=u'不可能重名的爱音则')#把红包消息通知给这个群
        userName = users[0]['UserName']#获取这个群的唯一标示
        for g in groups:
            if msg['FromUserName'] == g['UserName']:#根据群消息的FromUserName匹配是哪个群
                group_name = g['NickName']
        msgbody = u'有人在群"%s"发了红包,请立即打电话给我,让我去抢'%group_name
        itchat.send(msgbody,toUserName=userName) #告诉指定的好友群内有红包

# @itchat.msg_register([TEXT])
# def deal_with_msg(msg):
#     text = msg['Content']
#     if text == u'加群':
#         itchat.add_member_into_chatroom(get_group_id("小猪的Python学习交流群"),
#                                         [{'UserName': msg['FromUserName']}], useInvitation=True)
#     elif text == u'博客':
#         return 'coder-pig的个人主页-掘金：https://juejin.im/user/570afb741ea493005de84da3'
#     elif text == u'公众号':
#         itchat.send_image('gzh.jpg', msg['FromUserName'])
#     elif text == u'打赏':
#         itchat.send_image('ds.gif', msg['FromUserName'])
#         itchat.send_msg('您的打赏，会让小猪更有动力肝出\n更Interesting的文章，谢谢支持～', msg['FromUserName'])
#         itchat.send_image('wxpay.png', msg['FromUserName'])

# 处理微信公众号消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isMpChat=True)
def text_reply(msg):
    # 监听指定微信公众号推送的文章信息
    print(msg)
    if itchat.search_mps(name='双马尾萝莉')[0]["NickName"] == "双马尾萝莉":
        # 爬取的是itchat.search_mps(name='PythonCoder')[0]["NickName"]的公众号文章
        if msg["MsgType"] == 49:
            print("监听到指定微信公众号分享的文章链接：")
            # 拿到链接以后就可以获取到文章信息
            print(msg["Url"])
            userName1 = itchat.search_chatrooms(name=u'不可能重名的爱音则')
            itchat.send('公众号'+["NickName"] + '有新文章' + msg["Url"], toUserName=userName1)
        else:
            print("微信公众号分享的不是文章")
    elif itchat.search_mps(name='双马尾控')[0]["NickName"] == "双马尾控":
        if msg["MsgType"] == 49:
            print("监听到指定微信公众号分享的文章链接：")
            # 拿到链接以后就可以获取到文章信息
            print(msg["Url"])
            itchat.send('公众号'+["NickName"] + '有新文章' + msg["Url"], toUserName=userName)
        else:
            print("微信公众号分享的不是文章")
    elif itchat.search_mps(name='推大妞')[0]["NickName"] == "推大妞":
        if msg["MsgType"] == 49:
            print("监听到指定微信公众号分享的文章链接：")
            # 拿到链接以后就可以获取到文章信息
            print(msg["Url"])
            itchat.send('公众号'+["NickName"] + '有新文章' + msg["Url"], toUserName=userName)
        else:
            print("微信公众号分享的不是文章")
    elif itchat.search_mps(name='深夜十一点读书')[0]["NickName"] == "深夜十一点读书":
        if msg["MsgType"] == 49:
            print("监听到指定微信公众号分享的文章链接：")
            # 拿到链接以后就可以获取到文章信息
            print(msg["Url"])
            itchat.send('公众号'+["NickName"] + '有新文章' + msg["Url"], toUserName=userName)
        else:
            print("微信公众号分享的不是文章")
            itchat.send('微信公众号分享的不是文章', toUserName=userName)
    elif itchat.search_mps(name='MrXWLB')[0]["NickName"] == "MrXWLB":
        if msg["MsgType"] == 49:
            print("监听到指定微信公众号分享的文章链接：")
            # 拿到链接以后就可以获取到文章信息
            print(msg["Url"])
            itchat.send('公众号'+["NickName"] + '有新文章' + msg["Url"], toUserName=userName)
        else:
            print("微信公众号分享的不是文章")
    else:
        pass

itchat.auto_login(hotReload=True)
itchat.run()