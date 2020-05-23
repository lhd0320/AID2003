
file1=input('要备份的文件：')
file2=input('备份到哪里：')
fr=open(file1,'rb')
fw=open(file2,'wb')
while True:
    data=fr.read(1024)
    if not data:
        break
    fw.write(data)
fr.close()
fw.close()