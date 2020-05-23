"""
面向过程
    创建模块:module01,提供函数delete_duplicate,删除列表中重复元素
    [1,1,1,2,2,3,4,5,1,2,6] --> [1,2,3,4,5,6]
    建议：不使用集合set,自定义删除算法
    创建模块:module02,调用上面方法delete_duplicate
"""   # uniqueness 独一无二

list_duplicate=[1,1,1,2,2,3,4,5,1,2,6]
def delete_duplicate():
    global list_duplicate
    count=2
    for r01 in range(len(list_duplicate) - 1, -1, -1):
        for c01 in range(len(list_duplicate) - count, -1, -1):
            if list_duplicate[r01]==list_duplicate[c01]:
                del list_duplicate[c01]
                count+=1
    for r02 in range(len(list_duplicate)-1):
        for c02 in range(r02+1,len(list_duplicate)):
            if list_duplicate[r02]>list_duplicate[c02]:
                list_duplicate[r02],list_duplicate[c02]=list_duplicate[c02],list_duplicate[r02]
    return list_duplicate


