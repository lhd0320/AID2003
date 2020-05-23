import re
s="""Hello
北京
"""
# 只匹配英文
result=re.findall("\w+",s,re.A)

print(result)

# 让.可以匹配换行
result=re.findall(".+",s)
print(result)
result=re.findall(".+",s,re.S)
print(result)

#不区分大小写
result=re.findall("[a-z]+",s,re.I|re.A) # 同时添加多个拓展
print(result)

# ^能匹配每一行的开头，$能匹配每一行的结尾
result=re.findall("^北京",s,re.M)
print(result)