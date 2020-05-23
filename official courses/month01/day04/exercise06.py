# print(ord("刘"))
# print(chr(21016))

# message=input("请输入内容:")
# for char in message:
#         print(ord(char))

while True:
    if input("请输入回车键结束:"):
        coded_value=input("请输入一段编码值(十进制):")
        print(chr(int(coded_value)))
    else:
        break

while True:
    if input("请输入回车键结束:"):
        coded_value=input("请输入一段编码值(十六进制):")
        print(chr(int(coded_value,16)))
    else:
        break
