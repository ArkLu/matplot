# Ark Lu
# 2020-06-26

# Bs4 introduction: https://www.jianshu.com/p/fdee8d2be876
# Beautfiful Soup将复杂HTML文档转换成一个复杂的树形结构，
# 每个节点都是Python对象，所有对象可以归纳为4种：
# tag，NavigableString，BeautifulSoup，Comment。
import re

from bs4 import BeautifulSoup as bs

file = open("./baidu2.html", "rb")
html = file.read().decode('utf-8')
result = bs(html, "html.parser")
# print(result.head)
# 1Tag 标签及其第一个值
# print(type(result.head))   #Tag
#
# #N2avigableString
# print(type(result.title.string))
#
# print(result.a.attrs)

# 3.BeautifulSoup  -Document
# print(result)

# 4. <!--sijfjsdf-->Comment

# ---------
# 遍历文档
# print(result.head.contents)
# print(result.head.contents[0:3])

# 搜索文档- 字符串搜索
# find_all
# t_list = result.find_all('a')
# print(t_list)


# 正则表达式搜索 Search()
# t_list = result.find_all(re.compile('a'))  # Head/meta, including a
# print(t_list)


# 搜索按照函数方法
# def name_is_exist(tag):
#     return tag.has_attr('name')
#
#
# t_list = result.find_all(name_is_exist)
# for item in t_list:
#     print(item)

# 参数kwargs
# t_list = result.find_all(id="head")
# for item in t_list:
#     print(item)

# t_list = result.find_all(class_=True)  #class_后面带下划线，不是真正的class
# for item in t_list:
#     print(item)

# 按具体值找
#  t_list = result.find_all(href="//www.baidu.com/more/")

# Text找
# t_list = result.find_all(text=("百度", "地图"))

# 正则表达式，/d表示数字
#  t_list = result.find_all(text=re.compile("/d"))

# limit参数，表示结果只显示几个
# t_list = result.find_all(text=re.compile("/d"), limit=2)

# CSS 选择器
#  t_list = result.select("title")   #通过标签
# t_list = result.select(".mnav")    #通过类名
# t_list = result.select("#u1")     #通过id
# t_list = result.select("a[class='s-bri c-font-normal c-color-t']")  #通过属性进行查找
# t_list = result.select("head > meta")  # 通过子标签进行查找
t_list = result.select("a ~ div")  # 兄弟标签
print (t_list[5].get_text()) #得到相关文本
# for item in t_list:
#     print(item.get_text())
# for item in t_list:
#     print(item)
