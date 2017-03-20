import requests
import itchat
from itchat.content import *

#KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

# def get_response(msg):
#     '''
# 	构造图灵机器人返还的数据
# 	'''
#     apiUrl = 'http://www.tuling123.com/openapi/api'
#     data = {
#         'key'    : KEY,
#         'info'   : msg,
#         'userid' : 'wechat-robot',
#     }
#     try:
#         r = requests.post(apiUrl, data=data).json()
#         # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
#         return r.get('text')
#     # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
#     # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
#     except:
#         # 将会返回一个None
#         return


# @itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
# def tuling_reply(msg):
#     # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
# 	defaultReply = 'I received: ' + msg['Text']
# 	reply = get_response(msg['Text'])
# 	source = msg['FromUserName']
# 	#username = msg['ActualNickName']
# 	userid = msg['ToUserName']
# 	itchat.send(reply, source)



@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def register_reply(msg):
    if(msg['Text']=="打印名单"):
        student = ''
        source = msg['FromUserName']
        for i in range(len(itchat.get_contact())):            
            if(itchat.get_contact()[i]['UserName']==source):
                user_group = itchat.get_contact()[i]['MemberList']
                for j in range(len(user_group)):
                    student += user_group[j]['NickName'] + '\n'
        itchat.send(student, source)

itchat.auto_login(hotReload=True)
itchat.run()