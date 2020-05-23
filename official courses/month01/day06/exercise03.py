statement="To have a government that is of people by people for people"
list_statement=statement.split(" ")
list_new_statement=[]
for index in range(len(list_statement)-1,-1,-1):
    list_new_statement.append(list_statement[index])
str_statement=" ".join(list_new_statement)
print(str_statement)