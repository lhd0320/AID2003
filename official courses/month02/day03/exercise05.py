f=open('hello.py','w',buffering=1)
while True:
    print("="*50)
    msg=input('>>')
    if not msg:
        break
    data=f.write(msg+'\n')
f.close()