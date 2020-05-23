list_planet=["水星","金星","火星","木星"]
list_planet.insert(2,"地球")
list_planet.append("土星")
list_planet.append("天王星")
list_planet.append("海王星")
print(list_planet[0])
print(list_planet[-1])
print(list_planet[:2])
list_planet.remove("海王星")
del list_planet[3]
for index in range(len(list_planet)-1,-1,-1):
    print(list_planet[index])