from urllib.request import urlopen, quote
import json
import requests
import itchat
from itchat.content import *

def getlnglat(address):
    address = quote(address)
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'Uba11lIVgQGGj2xPZPif4mfRtNXjVhSo'
    uri = url + '?output=' + output + '&address=' + address + '&ak=' + ak
    # try:
    temp = urlopen(uri)
    temp = json.loads(temp.read().decode())
    # except:
    # temp = None
    # finally:
    return temp

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
            print(getlnglat(city))
        itchat.send(address_list, source)

itchat.auto_login(hotReload=True)
itchat.run()