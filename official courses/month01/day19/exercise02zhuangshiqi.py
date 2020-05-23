import time


def print_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        execute_time=time.time()-start_time
        print("执行时间%f"%(execute_time))
        return result
    return wrapper

@print_time
def sum_number(stop_value):
    sum_value=0
    for number in range(stop_value):
        sum_value+=stop_value
    return sum_value

sum_number(1000)

time_tuple=time.localtime()
print(time_tuple)

list01=["a","b"]
list01[:]="ppp"
list02=list01[:]
list02[0]="o"
print(list01)
print(list02)

class A:
    a=1
obj=A()
obj.a=2
print(obj.a)
print(A.a)
A.a=3
print(obj.a)

a=frozenset((1,2,3))
b={2,3,4}
print(a - b)

x=[1,'two',3,'Four']
y=[1,'two',3,'Four']
print(x[2:3]==3)
print(x[2:3])
print(x==y)

list=list(("aaa",))
print(list)