import re

def find_equipment_address():
    equipment=input("请输入设备名称：")
    f=open("/home/tarena/下载/month02/day04/log.txt","r")
    msg = f.read()
    result_paragraph = msg.split("\n\n")

    for index in range(1,len(result_paragraph)):
        sentence=result_paragraph[index].split(",")[0]
        equipment_word = sentence.split(" ")[0]
        if equipment==equipment_word:
            address=re.findall("address is \w{4}\.\w{4}.\w{4}",result_paragraph[index])
            return address
    return "Uknow"


print(find_equipment_address())