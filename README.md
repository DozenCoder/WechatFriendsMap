
`address` 通过`itchat`登录web微信获取好友地理位置信息，调用百度地图[Geocoding API](http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding),使用`Express`作为后端，`Echarts`展现前端，绘制微信好友地图(以好友微信设置地址为准，不包括海外地址及泛区域地址)。  
usage(仅在`python3.5`,`node8.2.1`,`Ubuntu16.04.2 LTS`下测试过，少数语法可能不兼容python2或低版本python3，Windows会有文件路径问题（懒得改了）):
```
>> git clone https://github.com/superPershing/WechatFriendsMap.git
>> cd WechatFriendsMap/
>> virtualenv venv -p python3
>> source venv/bin/activate
>> pip install -r requirements.txt
>> cd mapApp
>> npm install
>> cd ..
>> python3 address.py
```
扫描二维码，对自己(或其他好友对当前登录用户)发送`address`信息即会自动弹出浏览器，展示前端界面。  


示例：
![](map_instance.png)
