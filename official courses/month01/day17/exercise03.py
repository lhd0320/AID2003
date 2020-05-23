# class NumberIterator:
#     def __init__(self,data):
#         self.__data=data
#         self.__index = -1
#
#     def __next__(self):
#         try:
#             self.__index += 1
#             return self.__data[self.__index]
#         except IndexError:
#             raise StopIteration()
#
# class Myrange:
#     def __init__(self,stop_number):
#         self.__list_range=[]
#         count=0
#         while True:
#             if count<stop_number:
#                 self.__list_range.append(count)
#                 count+=1
#             else:
#                 break
#     def __iter__(self):
#         return NumberIterator(self.__list_range)
#
# for i in Myrange(5):
#     print(i)

# class NumberIterator:
#     def __init__(self,stop_number):
#         self.__stop_number = stop_number
#         self.__start_number=-1
#
#     def __next__(self):
#         self.__start_number += 1
#         if self.__start_number<self.__stop_number:
#             return self.__start_number
#         else:
#             raise StopIteration()
# class Myrange:
#     def __init__(self,number):
#         self.__number=number
#     def __iter__(self):
#         return NumberIterator(self.__number)
#
# for i in Myrange(5):
#     print(i)

# class Myrange:
#     def __init__(self,stop_number):
#         self.__list_range=[]
#         count=0
#         while True:
#             if count<stop_number:
#                 self.__list_range.append(count)
#                 count+=1
#             else:
#                 break
#     def __iter__(self):
#         # return NumberIterator(self.__list_range)
#         for i in self.__list_range:
#             yield  i
#
# for i in Myrange(5):
#     print(i)



class Myrange:
    def __init__(self,number):
        self.__number=number
    def __iter__(self):
        start=0
        while start<self.__number:
            yield start
            start+=1



for i in Myrange(5):
    print(i)


