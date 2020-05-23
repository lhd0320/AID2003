from multiprocessing import Pool
import os



def copy_file(old_path,new_path):
    # list_file=os.listdir('/home/tarena/PycharmProjects/official courses/month02/day12')
    list_file=os.listdir(old_path)
    for name in list_file:
        # f1=open('/home/tarena/PycharmProjects/official courses/month02/day12/%s'%(name),'r')
        fr=open('%s/%s'%(old_path,name),'rb')
        # f2 = open('/home/tarena/PycharmProjects/official courses/month02/day12/备份文件练习/%s' % (name), 'w')
        fw = open('%s/%s' % (new_path,name), 'wb')
        fw.write(fr.read())
        fr.close()
        fw.close()

def main():
    # os.mkdir('/home/tarena/PycharmProjects/official courses/month02/day12/备份文件练习')
    new_document='/home/tarena/PycharmProjects/official courses/month02/day13/备份文件练习'
    os.mkdir(new_document)
    old_path='/home/tarena/PycharmProjects/official courses/month02/day12'

    pool=Pool()
    pool.apply_async(func=copy_file,args=(old_path,new_document))
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()