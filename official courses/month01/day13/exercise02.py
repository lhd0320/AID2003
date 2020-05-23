# class Vector2:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return "%d   %d"%(self.x,self.y)
#     def __floordiv__(self, other):
#         return Vector2(self.x//other.x,self.y//other.y)
# v01=Vector2(6,9)
# v02=Vector2(2,3)
# result=v01//v02
# print(result)
#
# class Vector2:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return "%d   %d"%(self.x,self.y)
#     def __mod__(self, other):
#         return Vector2(self.x%other.x,self.y%other.y)
# v01=Vector2(6,9)
# print(v01.x)
# v02=Vector2(2,3)
# result=v01%v02
# print(result)
# print(v01)

# class Vector2:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return "%d   %d"%(self.x,self.y)
#     def __imod__(self, other):
#         # return Vector2(self.x%other.x,self.y%other.y)
#         self.x %= other.x
#         self.y %= other.y
#         return self
# v01=Vector2(6,9)
# print(v01.x)
# v02=Vector2(2,3)
# v01%=v02
# print(v01)
#
# class Vector2:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return "%d   %d"%(self.x,self.y)
#     def __isub__(self, other):
#         # return Vector2(self.x%other.x,self.y%other.y)
#         self.x -= other.x
#         self.y -= other.y
#         return self
# v01=Vector2(6,9)
# print(v01.x)
# v02=Vector2(2,3)
# v01-=v02
# print(v01)

class Vector2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
v01=Vector2(6,6)
v02=Vector2(6,6)
print(v01 == v02)