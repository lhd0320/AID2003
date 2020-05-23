f=open('hello.py','w')
while True:
    item=input("请按回车结束：")
    if item!='':
        n=f.write(item+'\n')
    else:
        break
f.close()