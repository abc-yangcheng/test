# -*- coding:utf-8 -*-

# @Time: 2024/1/9 11:29
# @Project: test
# @File: read_xml.py
# @Author: WSM
from xml.dom.minidom import parse

# 打开 XML 文件
dom = parse('./data_file/config.xml')
# 得到文档元素对象
root = dom.documentElement
# 获取(一组)标签
tag_name = root.getElementsByTagName('os')
print(tag_name[0].firstChild.data)
print(tag_name[1].firstChild.data)
print(tag_name[2].firstChild.data)

login_info = root.getElementsByTagName('login')
# 获得 login 标签的 username 属性值
username = login_info[0].getAttribute("username")
print(username)
# 获得 login 标签的 password 属性值
password = login_info[0].getAttribute("password")
print(password)
# 获得第二个 login 标签的 username 属性值
username = login_info[1].getAttribute("username")
print(username)
# 获得第二个 login 标签的 password 属性值
password = login_info[1].getAttribute("password")
print(password)
