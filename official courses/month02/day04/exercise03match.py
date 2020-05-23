import re
# result=re.finditer("(\w+):(\d+)","ALex:1997,Sunny:1995")
#
# for i in result:
#     print(i.group())

# 只匹配开头
# result = re.match("(\w+):(\d+)","ALex:1997,Sunny:1995")
# print(result.group())
# 匹配第一处内容
# result = re.search("(\w+):(\d+)"," ALex:1997,Sunny:1995")


# 获取match对象对应内容
result = re.search("(?P<name>\w+):(?P<year>\d+)","  ALex:1997,Sunny:1995")
print(result.group())
print(result.group(1))
print(result.group("year"))
print(result.group("name"))


print(result.span())

print(result.groupdict())