list01=[32,1,3,24,5,2]
i=list01.__iter__()
while True:
    try:
        item=i.__next__()
        print(item)
    except StopIteration:
        break


tuple01=(4,45,65,76,8)
i=tuple01.__iter__()
while True:
    try:
        item=i.__next__()
        print(item)
    except StopIteration:
        break

dict01={"a":3,"b":3,"c":2}
key=dict01.__iter__()
while True:
    try:
        k=key.__next__()
        print(k)
        print(dict01[k])
    except StopIteration:
        break

