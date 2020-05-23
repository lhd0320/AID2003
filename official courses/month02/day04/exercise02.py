import re
result=re.findall("\w+:\d+","ALex:1997,Sunny:1995")
print(result)
result=re.findall("(\w+):\d+","ALex:1997,Sunny:1995")
print(result)
result=re.findall("(\w+):(\d+)","ALex:1997,Sunny:1995")
print(result)
print("-"*50)

result=re.split(":|,","ALex:1997,Sunny:1995")
print(result)
result=re.split(":|,","ALex:1997,Sunny:1995",2)
print(result)
result=re.split(":|,","ALex:1997,Sunny:1995",1)
print(result)
print("-"*50)
result=re.sub("\d+","xxx","ALex:1997,Sunny:1995")
print(result)
result=re.sub("\d+"," ","ALex:1997,Sunny:1995",1)
print(result)