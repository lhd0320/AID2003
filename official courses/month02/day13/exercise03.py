from multiprocessing import Pool,Queue
import os

q=Queue()


def copy_file(name,old_path,new_path):
    # f1=open('/home/tarena/PycharmProjects/official courses/month02/day12/%s'%(name),'r')
    fr=open('%s/%s'%(old_path,name),'rb')
    # f2 = open('/home/tarena/PycharmProjects/official courses/month02/day12/备份文件练习/%s' % (name), 'w')
    fw = open('%s/%s' % (new_path,name), 'wb')
    while True:
        data=fr.read(1024)
        if not data:
            break
        n=fw.write(data)
        q.put(n)
    fr.close()
    fw.close()

def get_total_size(path):
    total_size=0
    for file in os.listdir(path):
        total_size+=os.path.getsize('%s/%s'%(path,file))
    return total_size

def main():
    # os.mkdir('/home/tarena/PycharmProjects/official courses/month02/day12/备份文件练习')
    new_document='/home/tarena/PycharmProjects/official courses/month02/day13/备份文件练习'
    os.mkdir(new_document)
    old_path='/home/tarena/PycharmProjects/official courses/month02/day12'
    total_size=get_total_size(old_path)


    pool=Pool()
    # list_file=os.listdir('/home/tarena/PycharmProjects/official courses/month02/day12')
    for name in os.listdir(old_path):
        pool.apply_async(func=copy_file,args=(name,old_path,new_document))

    copy_size = 0
    while copy_size<total_size:
        copy_size+=q.get()
        print("拷贝进度：%.2f%%"%(copy_size/total_size*100))

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()