import requests
import itchat
from itchat.content import *

@itchat.msg_register(itchat.content.TEXT)
def address_reply(msg):
    if(msg['Text']=="address"):
        source = msg['FromUserName']
        address = itchat.get_friends(update=False)
        print(type(address))
        address_list = ''
        for i in address:
            nickname = i["NickName"]
            city = i["City"]
            province = i["Province"]
            address_i = nickname + ':' + province + ' ' + city
            address_list += address_i + '\n'
        itchat.send(address_list, source)

itchat.auto_login(hotReload=True)
itchat.run()