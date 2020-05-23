# import re
# a=re.search("a","<a>wahaha</a>").group()
# print(a)
#
# b=re.search("h1","<h1>qqxing</h1>").group()
# print(b)

# print("aaa\nbbb",end="")
# print("aaa\nbbb")


# n=[5,9,7,1,1,1,9,7,5,5,5]
# list_num=[]
#
# for r in n:
#     count=0
#     for c in n:
#         if r==c:
#             count+=1
#     if count%2!=0 and r not in list_num:
#         list_num.append(r)
# print(list_num)

# marix=[
# [2,3,4,5],
# [13,14,17,19],
# [25,26,27,28],
# ]
# target=17
# row=len(marix) # 行
# col=len(marix[0]) # 列
# i=row-1
# j=0
# judge=False
# while (i>=0)or(j<col):
#     if i < 0 or j > (col-1):
#         break
#     if marix[i][j]>target:
#         i=i-1
#     elif marix[i][j]<target:
#         j=j+1
#     elif marix[i][j]==target:
#         judge=True
#         break
# print(judge)


# [
#     [0,0,0,0],
#     [0,0,0,0]
# ]

file_list=['a','s','w','q']
files="\n".join(file_list)
print(files)