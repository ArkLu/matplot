# Ark Lu
# 2020-06-29


import re

pat = re.compile("AA*")  # AA is 正则表达式，去验证其他的字符串结果

m = pat.search("ABCAADDCC")  # Search 字符串娇艳的内容进行比对查找 ，找到第一个结果

n = re.search('aa?', 'khjjhdaa')  # 前面为规则，后面为查找对象

# t = re.findall('a', 'hjjhakkijA aaa iia')
# t = re.findall('[a-z]', 'hjjhakkijA aaa iia')
# t = re.sub('a', 'A', 'hjjhakkijA aaa iia')              # 替换字符

t = r'\shhuur\'u'       # 字符串前面加r 里面特殊字符不会转译

# print(m)
#
# print(n)
print(t)
