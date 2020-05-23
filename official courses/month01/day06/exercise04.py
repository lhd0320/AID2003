# list_content=[]
# for item in range(1,51):
#     if item % 3 == 0 or item % 5 == 0:
#         list_content.append(item)
# print(list_content)
list_content=[item for item in range(1,51) if item % 3 == 0 or item % 5 == 0]
print(list_content)

# list_content=[]
# for item in range(5,101):
#         list_content.append(item**2)
# print(list_content)
list_content=[item**2 for item in range(5,101)]
print(list_content)
